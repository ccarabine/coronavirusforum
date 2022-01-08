from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    model = Post
    latest_posts_queryset = Post.objects.order_by('-created')[:5]
    queryset = Post.objects.order_by('-created')
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 5
