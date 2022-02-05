# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import F, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic import DeleteView, CreateView

from json import dumps
from requests import get

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .forms import PostForm, CommentForm
from .models import Post, Topic, Comment, Vote


def error_404_view(request, exception):
    """
    A view to render 404 error page if the user goes to a non-exist url
    Args:
        request (object): HTTP request object.
        exception: exception error
    Returns:
        Render 404error page
    """
    return render(request, '404error.html', status=404)


def error_500_view(request):
    """
    A view to render 500 error page if there is a server error such
    as the api failing
    Args:
        request (object): HTTP request object.
    Returns:
        Render 500error page
    """
    return render(request, '500error.html', status=500)


class PostListHomeView(ListView):
    """
    A view to show 5 lastest posts ordered by created
    Args:
        ListView: class based view
    Returns:
        Render of home page with context
    """
    model = Post
    queryset = Post.objects.order_by("-created")[:5]
    template_name = "index.html"
    context_object_name = "latest_posts"


class PostListView(ListView):
    """
    A view to show 5 lastest posts filtered by topic
    Args:
        ListView: class based view
    Returns:
        Render of post list with context
    """
    template_name = "postlist.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):  # get all the posts by topic
        queryset = Post.objects.filter(topic__slug=self.kwargs["topic"])
        return queryset

    def get_context_data(self, **kwargs):  # to get the topic selected
        context = super().get_context_data(**kwargs)
        context["topic"] = Topic.objects.get(slug=self.kwargs["topic"])
        return context


def topic_list(request):
    """
    A view to show the topic list for the navbar
    Args:
        request (object): HTTP request object.
    Returns:
        context
    """
    topic_list = Topic.objects.exclude(name="default")
    context = {
        "topic_list": topic_list,
    }
    return context


class PostDetailView(DetailView):
    """
    A view to show individual post, detail
    paginates 5 comments per page
    Update the variables, whether the user has voted and if they have upvoted
    Args:
        DetailView: class based view
    Returns:
        Render of post detail with context
    """
    model = Post
    template_name = "postdetail.html"

    def get_context_data(self, **kwargs):
        # Comment pagination section
        context = super(PostDetailView, self).get_context_data(**kwargs)
        page = self.request.GET.get("page")
        paginator = Paginator(self.object.comment_post.all(), 5)
        pk = self.kwargs["pk"]
        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = self.object.comment_post.all()

        # Votes section
        voted = False
        upvoted = None
        if self.request.user in post.votes.all():
            voted = True
            upvoted = Vote.objects.get(post=post, user=self.request.user).vote
        context["page"] = page
        context["paginator"] = paginator
        context["object_list"] = context["paginator"].get_page(context["page"])
        context["page_obj"] = paginator.get_page(page)
        context["post"] = post
        context["comments"] = comments
        context["form"] = form
        context["voted"] = voted
        context["upvoted"] = upvoted
        return context


def addPost(request, topic):
    """
    A view to add a post, redirects to the post when submitted
    Args:
        request (object): HTTP request object.
        topic: topic
    Returns:
        Render of post form with context
    """
    if not request.user.is_authenticated:
        messages.error(
            request, 'Sorry, only logged in users can create a post.')
        return redirect(reverse('home'))
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        topic_obj = get_object_or_404(Topic, name=topic)

        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(request.POST["title"])
            post.owner = request.user
            post.user_name = request.user.username
            post.topic = topic_obj
            post.post_image = request.FILES.get("post_image")
            post.owner = request.user
            post.save()
            messages.success(request, 'Post submitted')
            return redirect(reverse("postdetail", args=[post.id]))
    context = {"form": form, "topic": topic}
    return render(request, "postform.html", context)


@method_decorator(login_required, name='dispatch')
class UpdatePostView(SuccessMessageMixin, UpdateView):
    """
    A view to edit a post
    Args:
        SuccessMessageMixin: SuccessMessageMixin (success message attribute)
        UpdateView: class based view
    Returns:
        Render of update post with success message
    """
    model = Post
    form_class = PostForm
    template_name = "updatepost.html"
    success_message = "Post updated"

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(owner=owner)


@method_decorator(login_required, name='dispatch')
class DeletePostView(SuccessMessageMixin, DeleteView):
    """
    A view to delete a post
    Args:
        SuccessMessageMixin: SuccessMessageMixin (success message attribute)
        DeleteView: class based view
    Returns:
        Render of delete post with success message
    """
    model = Post
    template_name = "deletepost.html"
    success_url = reverse_lazy("home")
    success_message = "Post deleted"


@method_decorator(login_required, name='dispatch')
class AddCommentView(SuccessMessageMixin, CreateView):
    """
    A view to add a comment
    Args:
        SuccessMessageMixin: SuccessMessageMixin (success message attribute)
        CreateView: class based view
    Returns:
        Render of comment form with success message and context
    """
    model = Comment
    form_class = CommentForm
    template_name = "commentform.html"
    success_message = "Comment added"

    def form_valid(self, form):
        """
        Set the post id and name to self instances
        Returns form
        Args:
            self (object): self.
            form (object): form.
        Returns:
            The form
        """
        form.instance.post_id = self.kwargs["pk"]
        form.instance.name = self.request.user.username
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Gets the post, returns context
        Args:
            self (object): Self object
            **kwargs: **kwargs
        Returns:
            Context
        """
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        kwargs["post"] = post
        return super().get_context_data(**kwargs)


def email_success(request):
    """
    After receiving and interpreting a request message,
    a server responds with the HTTP response message.
    Args:
       request (object): HTTP request object.
    Returns:
       HttpResponse
    """
    res = "Email is verified!"
    return HttpResponse("<p>%s</p>" % res)


@login_required
def VoteView(request, pk):
    """
   A view to add, edit and remove a vote
   redirects to the same post they are on
    Args:
       request (object): HTTP request object.
       pk:pk
    Returns:
       Render postdetail page
    """
    # get the post id from the form submit
    post = get_object_or_404(Post, pk=pk)
    id = post.id
    update = Post.objects.get(id=id)

    # get the check box value either on or none
    upVote = request.POST.get('upVote')
    downVote = request.POST.get('downVote')

    # check if the user exists in the post model votes true or false
    if update.votes.filter(id=request.user.id).exists():

        # Query to get the vote - True or false
        q = Vote.objects.get(Q(post_id=id) & Q(user_id=request.user.id))
        existing_vote = q.vote

        # user has voted
        if existing_vote:
            # Existing user has an upvote, deselected upvote
            # user has not voted
            if upVote == 'on':
                update.upvote = F('upvote') - 1
                update.votes.remove(request.user)
                update.save()
                update.refresh_from_db()
                q.delete()
                messages.success(request, 'Thumbs Up deselected')
            # Existing user has an upvote, selected downvote
            if downVote == 'on':
                update.upvote = F('upvote') - 1
                update.downvote = F('downvote') + 1
                update.save()
                q.vote = False
                q.save(update_fields=['vote'])
                update.refresh_from_db()
                messages.success(request, 'Thumbs Down selected')
        else:
            # existing user has an downvote, selected upvote
            if upVote == 'on':
                update.upvote = F('upvote') + 1
                update.downvote = F('downvote') - 1
                update.save()

                # Update Vote
                q.vote = True
                q.save(update_fields=['vote'])
                update.refresh_from_db()
                messages.success(request, 'Thumbs Up selected')

            # User has an exisiting downvote, De-selected downvote
            # User has not voted
            if downVote == 'on':
                update.downvote = F('downvote') - 1
                update.votes.remove(request.user)
                update.save()
                update.refresh_from_db()
                q.delete()
                messages.success(request, ' Thumbs Down deselected')
    else:
        # user has not voted - new vote - selected upvote
        if upVote == 'on':
            update.upvote = F('upvote') + 1
            update.votes.add(request.user)
            update.save()

            # Add new vote
            new = Vote(post_id=id, user_id=request.user.id, vote=True)
            new.save()
            messages.success(request, 'Thumbs Up selected')
        else:
            # user has not voted - new vote - selected downvote
            update.downvote = F('downvote') + 1
            update.votes.add(request.user)
            update.save()
            messages.success(request, 'Thumbs down selected')
            # Add new vote
            new = Vote(post_id=id, user_id=request.user.id, vote=False)
            new.save()

    # Return updated votes
    update.refresh_from_db()
    return HttpResponseRedirect(reverse('postdetail', args=[str(pk)]))


@login_required
def ContactUsReportView(request, slug):
    """
    Sends email -contact us form fields to admin or prints to the terminal
    in development
    Prepopulates email and username
    Args:
       request (object): HTTP request object.
       slug: slug
    Returns:
       Render contact us page  with context
    """
    email = request.user.email
    username = request.user.username

    if request.method == "POST":
        message_subject_a = request.POST['message-subject-display']
        message_email = request.POST['message-email']
        message_body = request.POST['message']
        send_mail(
            message_subject_a,
            message_body,
            message_email,
            ['projectckcabs@gmail.com'],
        )
        messages.success(request, 'Email sent successfully')
        return render(request, 'contactus.html', {'username': username})
    else:
        print(username)
        return render(request, 'contactus.html',
                      {'slug': slug, 'email': email})


def ContactUsView(request):
    """
    Sends email -contact us form fields to admin or prints to the terminal
    in development
    Args:
       request (object): HTTP request object.
    Returns:
       Render contact us page
    """
    username = request.user.username
    if request.method == "POST":
        message_subject = request.POST['message-subject']
        message_body = request.POST['message']
        message_email = request.POST['message-email']

        send_mail(
            message_subject,
            message_body,
            message_email,
            ['projectckcabs@gmail.com'],
        )
        messages.success(request, 'Email sent successfully')
        return render(request, 'contactus.html',
                      {'username': username})
    else:
        return render(request, 'contactus.html', {})


class SearchPostsView(ListView):
    """
    Search post model title field with the query and paginate by 5 posts
    Args:
      ListView: Class based view
    Returns:
       Render postlist page
    """
    model = Post
    template_name = "postlist.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):  # get all the posts by query
        """
        Filters the post by the query
        Args:
            self (object): Self object
        Returns:
            object_list: object_list
        """
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

    def get_context_data(self, **kwargs):
        """
        Gets the post, returns context
        Args:
            self (object): Self object
            **kwargs: **kwargs
        Returns:
            Context
        """
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get('q')
        return context


# "ENDPOINT and response code taken from
# https://coronavirus.data.gov.uk/details/developers-guide/main-api"
def apiview(request):
    """
    Try:
        gets the endpoint, filters by area type and name, structures the data
        puts the response into json
        put min and max dates into variables into the context
        gets the data for selected date
        returns govuk data page with context
    Except:
        return 500 error page
    Args:
      request (object): HTTP request object.
    """
    try:
        ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
        AREA_TYPE = "nation"
        AREA_NAME = "england"

        filters = [
            f"areaType={ AREA_TYPE }",
            f"areaName={ AREA_NAME }"
        ]

        structure = {
            "date": "date",
            "name": "areaName",
            "code": "areaCode",
            "dailyCases": "newCasesByPublishDate",
            "cumulativeCases": "cumCasesByPublishDate",
            "dailyDeaths": "newDeaths28DaysByPublishDate",
            "cumulativeDeaths": "cumDeaths28DaysByPublishDate"
        }

        api_params = {
            "filters": str.join(";", filters),
            "structure": dumps(structure, separators=(",", ":"))
        }

        response = get(ENDPOINT, params=api_params, timeout=10)

        responseapi = response.json()

        datelist = []
        for x in range(0, 100):
            datelist.append(responseapi['data'][x]['date'])

        mindate = min(datelist)
        maxdate = max(datelist)
        selecteddate = maxdate
        formpost = False

        if request.method == "POST":
            formpost = True
            selecteddate = request.POST['selecteddate']
            for x in range(0, 200):
                if selecteddate == responseapi['data'][x]['date']:
                    date = (responseapi['data'][x]['date'])
                    name = (responseapi['data'][x]['name'])
                    dailyCases = (responseapi['data'][x]['dailyCases'])
                    cumulativeCases = (
                        responseapi['data'][x]['cumulativeCases'])
                    dailyDeaths = (responseapi['data'][x]['dailyDeaths'])
                    cumulativeDeaths = (
                        responseapi['data'][x]['cumulativeDeaths'])

            context = {'formpost': formpost,
                       'datelist': datelist,
                       'date': date,
                       'name': name,
                       'dailyCases': dailyCases,
                       'cumulativeCases': cumulativeCases,
                       'dailyDeaths': dailyDeaths,
                       'cumulativeDeaths': cumulativeDeaths,
                       'mindate': mindate,
                       'maxdate': maxdate,
                       'selecteddate': selecteddate
                       }
            return render(request, 'govukdata.html', context)

        context = {'datelist': datelist,
                   'mindate': mindate,
                   'maxdate': maxdate,
                   'selecteddate': selecteddate
                   }
        return render(request, 'govukdata.html', context)
    except Exception:
        return render(request, '500error.html')


def AboutUsView(request):
    """
    Renders the about us page
    Args:
        request (object): HTTP request object.
    Returns:
        render about us page
    """
    return render(request, 'aboutus.html')


def TalkGuideLinesView(request):
    """
    Renders the talkguidelines page
    Args:
        request (object): HTTP request object.
    Returns:
        render talkguidelines page
    """
    return render(request, 'talkguidelines.html')


def PrivacyView(request):
    """
    Renders the privacy page
    Args:
        request (object): HTTP request object.
    Returns:
        render privacy page
    """
    return render(request, 'privacypolicy.html')
