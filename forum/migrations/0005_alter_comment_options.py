# Generated by Django 4.0.1 on 2022-01-19 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0004_post_enable_voting"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["-created"],
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
    ]