from . import views

from django.urls import path

urlpatterns = [
    path("", views.PostListHomeView.as_view(), name="home"),
    path("topic/<topic>/", views.PostListView.as_view(), name="topic"),
    path("topic/<int:pk>", views.PostDetailView.as_view(), name="postdetail"),
    path("addpost/<topic>/", views.addPost, name="addpost"),
    path("topic/update/<int:pk>", views.UpdatePostView.as_view(), name="updatepost"),
    path("topic/<int:pk>/remove", views.DeletePostView.as_view(), name="deletepost"),
    path("topic/<int:pk>/comment/", views.AddCommentView.as_view(), name="addcomment"),
    path("email_success/", views.email_success, name="email_success"),
    path("like/<int:pk>", views.UpVoteView, name="like_post"),
    
]
