from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic import DeleteView, CreateView
from django.template.defaultfilters import slugify
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.core.mail import send_mail

from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F, Q

from requests import get
from json import dumps

from .models import Post, Topic, Comment, Vote
from .forms import PostForm, CommentForm


def error_404_view(request, exception):
    return render(request, '404error.html',status=404)


def error_500_view(request):
    return render(request, '500error.html', status=500)


class PostListHomeView(ListView):
    model = Post
    queryset = Post.objects.order_by("-created")[:5]
    template_name = "index.html"
    context_object_name = "latest_posts"


class PostListView(ListView):

    template_name = "postlist.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):  # get all the posts by topic
        queryset = Post.objects.filter(topic__name=self.kwargs["topic"])
        return queryset

    def get_context_data(self, **kwargs):  # to get the topic selected
        context = super().get_context_data(**kwargs)
        context["topic"] = self.kwargs["topic"]
        return context


def topic_list(request):  # gets the topic list for the navbar
    topic_list = Topic.objects.exclude(name="default")
    context = {
        "topic_list": topic_list,
    }
    return context


class PostDetailView(DetailView):
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
            return redirect(reverse("postdetail", args=[post.id]))
    context = {"form": form, "topic": topic}
    return render(request, "postform.html", context)


class UpdatePostView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "updatepost.html"
    success_message = "Post updated"


class DeletePostView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = "deletepost.html"
    success_url = reverse_lazy("home")
    success_message = "Post deleted"


class AddCommentView(SuccessMessageMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "commentform.html"
    success_message = "Comment added"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        form.instance.name = self.request.user.username
        return super().form_valid(form)

    def get_context_data(self, **kwargs):  # Get the post
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        kwargs["post"] = post
        return super().get_context_data(**kwargs)


def email_success(request):
    res = "Email is verified!"
    return HttpResponse("<p>%s</p>" % res)


def VoteView(request, pk):
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
            # Existing user has an upvote, selected downvote
            if downVote == 'on':
                update.upvote = F('upvote') - 1
                update.downvote = F('downvote') + 1
                update.save()
                q.vote = False
                q.save(update_fields=['vote'])
                update.refresh_from_db()
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

            # User has an exisiting downvote, De-selected downvote
            # User has not voted
            if downVote == 'on':
                update.downvote = F('downvote') - 1
                update.votes.remove(request.user)
                update.save()
                update.refresh_from_db()
                q.delete()
    else:
        # user has not voted - new vote - selected upvote
        if upVote == 'on':
            update.upvote = F('upvote') + 1
            update.votes.add(request.user)
            update.save()

            # Add new vote
            new = Vote(post_id=id, user_id=request.user.id, vote=True)
            new.save()
        else:
            # user has not voted - new vote - selected downvote
            update.downvote = F('downvote') + 1
            update.votes.add(request.user)
            update.save()

            # Add new vote
            new = Vote(post_id=id, user_id=request.user.id, vote=False)
            new.save()

    # Return updated votes
    update.refresh_from_db()
    return HttpResponseRedirect(reverse('postdetail', args=[str(pk)]))


@login_required
def ContactUsReportView(request, slug):
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
    model = Post
    template_name = "postlist.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):  # get all the posts by query
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get('q')
        return context


# "ENDPOINT and response code taken from
# https://coronavirus.data.gov.uk/details/developers-guide/main-api"
def apiview(request):
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
    except Exception as e:
        context = {'e': e}
        return render(request, '500error.html', context)


def AboutUsView(request):
    return render(request, 'aboutus.html')

def TalkGuideLinesView(request):
    return render(request, 'talkguidelines.html')

def PrivacyView(request):
    return render(request, 'privacypolicy.html')
