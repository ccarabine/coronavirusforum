# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(verbose_name=("name"), max_length=100)

    def __str__(self):
        return str(self.name)


class Post(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, default=1)
    title = models.CharField(verbose_name=(
        "title"), max_length=200, unique=True)
    body = models.TextField(verbose_name=("body"), blank=True)
    user_name = models.CharField(
        verbose_name=("user_name"), max_length=200, blank=True, null=True
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_owner")
    slug = models.SlugField(verbose_name=("slug"), max_length=150, unique=True)
    updated = models.DateTimeField(verbose_name=("updated"), auto_now=True)
    created = models.DateTimeField(verbose_name=("created"), auto_now_add=True)
    post_image = models.ImageField(
        verbose_name=("post_image"), null=True, blank=True, upload_to=""
    )
    enable_voting = models.BooleanField(
        verbose_name=("enable_voting"), default=False)
    upvote = models.IntegerField(verbose_name=("upvote"), default="0")
    downvote = models.IntegerField(verbose_name=("downvote"), default="0")
    votes = models.ManyToManyField(
        User, related_name="post_votes", default=None, blank=True
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created"]

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return f"/topic/{self.pk}"


class Vote(models.Model):

    post = models.ForeignKey(
        Post,
        related_name="vote_post",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
    )
    user = models.ForeignKey(
        User,
        related_name="vote_user",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
    )
    vote = models.BooleanField(verbose_name=("vote"), default=True)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comment_post"
    )
    name = models.CharField(verbose_name=("name"), max_length=80)
    comment_body = models.TextField(
        verbose_name=("comment_body"),
    )
    created = models.DateTimeField(verbose_name=("created"), auto_now_add=True)

    class Meta:
        ordering = ["created"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-created"]

    def __str__(self):
        return f"Comment {self.comment_body} by {self.name}"

    def get_absolute_url(self):
        return f"/topic/{self.post_id}"
