from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostListHome.as_view(), name='home'),
    path('postlist', views.PostList.as_view(), name='postlist'),
]
