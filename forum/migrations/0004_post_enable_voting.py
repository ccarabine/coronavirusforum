# Generated by Django 4.0.1 on 2022-01-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_remove_post_excerpt_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='enable_voting',
            field=models.BooleanField(default=False, verbose_name='enable_voting'),
        ),
    ]
