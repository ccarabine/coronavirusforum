from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic import DeleteView, CreateView
from django.template.defaultfilters import slugify
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

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
        #stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_votes = post.total_votes()
        
        
        liked = False
        if post.votes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["total_votes"] = total_votes
        context["liked"] = liked
        
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


def UpVoteView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id')) #get the post id from the form submit
    liked = False
    if post.votes.filter(id=request.user.id).exists():
        post.votes.remove(request.user)
        liked=False
    else:
  
        post.votes.add(request.user)
    
        liked=True
    return HttpResponseRedirect(reverse('postdetail', args=[str(pk)]))

   
