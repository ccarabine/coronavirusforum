from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, DetailView
from .models import Post


class PostListHome(ListView):
    model = Post
    queryset = Post.objects.order_by('-created')[:5]
    template_name = 'index.html'
    context_object_name = 'latest_posts'

class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by('-created')
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    paginate_by = 5