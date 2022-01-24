from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic import DeleteView, CreateView
from django.template.defaultfilters import slugify
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F, Q
from django.core import serializers
from .models import Post, Topic, Comment, Vote
from .forms import PostForm, CommentForm


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
        context = super(PostDetailView, self).get_context_data(**kwargs)
        page = self.request.GET.get("page")
        paginator = Paginator(self.object.comment_post.all(), 5)
        context["page"] = page
        context["paginator"] = paginator
        context["object_list"] = context["paginator"].get_page(context["page"])
        context["page_obj"] = paginator.get_page(page)

        pk = self.kwargs["pk"]
        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = self.object.comment_post.all()

        # need to pass into the total votes
        # stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_votes = post.total_votes()
        
        voted = False
        upvoted = None
        
        if self.request.user in post.votes.all():
            voted = True
            upvoted = Vote.objects.get(post=post, user=self.request.user).vote

        context["total_votes"] = total_votes
        context["voted"] = voted
        context["upvoted"] = upvoted

        context["post"] = post
        context["comments"] = comments
        context["form"] = form
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
    voteUser = request.user
    upVote = request.POST.get('upVote')
    downVote = request.POST.get('downVote')
   
    # icheck if there is  user in the post model votes
    if update.votes.filter(id=request.user.id).exists():
        # Get the users current vote (True/False) & query
        print('START HERE')
        
        q = Vote.objects.get(
        Q(post_id=id) & Q(user_id=request.user.id))
        existing_vote = q.vote  # true or false

        if existing_vote == True:
            print(f'{existing_vote} existing user has voted')
                
            print(f'{upVote} upvote {downVote} downvote')
            if upVote == 'on':
                print("exsiting user has voted, deslected upvote")
                update.upvote = F('upvote') - 1
                update.votes.remove(request.user)
                update.save()
                update.refresh_from_db()
                print(f'{upVote} upvote {downVote} downvote')
                q.delete()

            if downVote == 'on':
                # Change vote in Post
                print("exsiting user has voted, deselected upvote?now clicked on downvote -checked box on")
                update.upvote = F('upvote') - 1
                update.downvote = F('downvote') + 1
                update.save()

                # update vote
                q.vote = False
                q.save(update_fields=['vote'])

                # Return updated votes
                update.refresh_from_db()
                print(f'{upVote} upvote {downVote} downvote')

        elif existing_vote == False:
            print("exisiting vote false")
            if upVote == 'on':
                # Change vote in Post
                print("we have an upvote - on")
                update.upvote = F('upvote') + 1
                update.downvote = F('downvote') - 1
                update.save()

                # Update Vote

                q.vote = True
                q.save(update_fields=['vote'])

                # Return updated votes
                update.refresh_from_db()
                print(f'{upVote} upvote {downVote} downvote')
            if downVote == 'on':


                print("we have an downvote - on")
                update.downvote = F('downvote') - 1
                update.votes.remove(request.user)
                update.save()
                update.refresh_from_db()
                q.delete()
                print(f'{upVote} upvote {downVote} downvote')
                
    else:
        
        if upVote == 'on':
            print("new selection - user pressed upvote")
            
            update.upvote = F('upvote') + 1
            update.votes.add(request.user)
            update.save()

            # Add new vote
            new = Vote(post_id=id, user_id=request.user.id, vote=True)
            new.save()
            print(f'{upVote} upvote {downVote} downvote')
        else:
            print("new selection - user pressed downvote")
            
            update.downvote = F('downvote') + 1
            update.votes.add(request.user)
            update.save()
            # Add new vote
            new = Vote(post_id=id, user_id=request.user.id, vote=False)
            new.save()
            print(f'{upVote} upvote {downVote} downvote')
   

    # Return updated votes
    up_vote=post.upvote
    print(up_vote)
    update.refresh_from_db()

    request.session['upVote'] = upVote
    request.session['downVote'] = downVote
    print("END")
    return HttpResponseRedirect(reverse('postdetail', args=[str(pk)]))
    