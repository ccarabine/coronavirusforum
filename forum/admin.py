from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
from . import models


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "topic", "owner", "created")
    search_fields = ["title", "content"]
    summernote_fields = ("excerpt",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "comment_body", "post", "created")
    search_fields = ("name", "body")


admin.site.register(models.Topic)
