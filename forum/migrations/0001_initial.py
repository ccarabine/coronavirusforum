# Generated by Django 4.0.1 on 2022-02-03 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='title')),
                ('body', models.TextField(blank=True, verbose_name='body')),
                ('user_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='user_name')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='slug')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='post_image')),
                ('enable_voting', models.BooleanField(default=False, verbose_name='enable_voting')),
                ('upvote', models.IntegerField(default='0', verbose_name='upvote')),
                ('downvote', models.IntegerField(default='0', verbose_name='downvote')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField(default=True, verbose_name='vote')),
                ('post', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='vote_post', to='forum.post')),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='vote_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vote',
                'verbose_name_plural': 'Votes',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='forum.topic'),
        ),
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.ManyToManyField(blank=True, default=None, related_name='post_votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('comment_body', models.TextField(verbose_name='comment_body')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='forum.post')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['created'],
            },
        ),
    ]
