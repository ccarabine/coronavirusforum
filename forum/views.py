from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView

from .models import Post, Topic


class PostListHome(ListView):
    model = Post
    queryset = Post.objects.order_by('-created')[:5]
    template_name = 'index.html'
    context_object_name = 'latest_posts'


class PostList(ListView):
    template_name = 'postlist.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):  #get all the posts by topic
        queryset = Post.objects.filter(topic__name=self.kwargs["topic"])
        return queryset
        

def topic_list(request):  # gets the topic list for the navbar
    topic_list = Topic.objects.exclude(name='default')
    context = {
        "topic_list": topic_list,
    }
    return context

class PostDetail(DetailView):
    model = Post
    template_name = "postdetail.html"
    
   # def get(self, request, slug, *args, **kwarg):
   #     queryset = Post.objects
   #     post = get_object_or_404(queryset, slug=slug)
   #     comment = post.comments.order_by('created')