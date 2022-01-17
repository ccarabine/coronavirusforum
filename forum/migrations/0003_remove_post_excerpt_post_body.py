# Generated by Django 4.0.1 on 2022-01-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, verbose_name='body'),
        ),
    ]