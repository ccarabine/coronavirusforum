# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Post, Comment, Vote
from . import models


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin class for the post model.
    """
    prepopulated_fields = {
        "slug": ("title",),
    }
    list_display = (
        "title",
        "topic",
        "owner",
        "created"
        )
    search_fields = (
        "title",
        "topic"
        )
    summernote_fields = ("excerpt",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for the comment model.
    """
    list_display = (
        "name",
        "comment_body",
        "post",
        "created"
        )
    search_fields = (
        "name",
        "body"
        )


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    """
    Admin class for the vote model.
    """
    list_display = (
        "post",
        "user",
        "vote"
        )
    search_fields = (
        "post",
        "user"
        )


admin.site.register(models.Topic)
