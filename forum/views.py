from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from .models import Post, Topic


class PostListHome(ListView):
    model = Post
    queryset = Post.objects.order_by('-created')[:5]
    template_name = 'index.html'
    context_object_name = 'latest_posts'


class PostList(ListView):
    template_name = 'postlist.html'
    context_object_name = 'post_list'
   # paginate_by = 5 NEED TO FIX

    def get_queryset(self): #get all the posts by topic
        content = {
            'top': self.kwargs['topic'],
            'posts': Post.objects.filter(topic__name=self.kwargs['topic'])
            }
        return content


def topic_list(request):  # gets the topic list for the navbar
    topic_list = Topic.objects.exclude(name='default')
    context = {
        "topic_list": topic_list,
    }
    return context
