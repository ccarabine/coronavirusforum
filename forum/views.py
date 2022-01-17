from django.views.generic import ListView, DetailView, UpdateView
from django.template.defaultfilters import slugify
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post, Topic
from.forms import PostForm


class PostListHomeView(ListView):
    model = Post
    queryset = Post.objects.order_by('-created')[:5]
    template_name = 'index.html'
    context_object_name = 'latest_posts'


class PostListView(ListView):
    template_name = 'postlist.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):  # get all the posts by topic
        queryset = Post.objects.filter(topic__name=self.kwargs["topic"])
        return queryset

    def get_context_data(self, **kwargs):  # to get the topic selected
        context = super().get_context_data(**kwargs)
        context['topic'] = self.kwargs['topic']
        return context


def topic_list(request):  # gets the topic list for the navbar
    topic_list = Topic.objects.exclude(name='default')
    context = {
        "topic_list": topic_list,
    }
    return context


class PostDetailView(DetailView):
    model = Post
    template_name = "postdetail.html"


def addPost(request, topic):
    form = PostForm()
    if request.method == 'POST':
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
            return redirect(reverse('postdetail', args=[post.id]))
    context = {'form': form, 'topic': topic}
    return render(request, "postform.html", context)

class UpdatePostView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'updatepost.html'
    success_message = 'Post updated'
    #fields = ('title', 'body', 'post_image',
     #         'enable_voting')

