# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase

# Internal:
from .models import Post, Topic, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestForumModels(TestCase):
    """
    A class for testing forum models
    """
    def setUp(self):
        """
        Create test user, topic, post and comment
        """
        user_b = User.objects.create_user(
            username='userb', password='p2word')

        topic = Topic.objects.create(
            name='coronavirus',
            slug='coronavirus',
            )

        post = Post.objects.create(
            topic=topic,
            title="Corona",
            owner=user_b,
            slug="Corona",
        )

        Comment.objects.create(
            post=post,
            name=user_b,
            comment_body="Test comment body",
        )

    def tearDown(self):
        """
        Delete test user, category, product and review
        """
        User.objects.all().delete()
        Topic.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()

    def test_topic_str_method(self):
        """
        This test tests the topic str method and verifies
        """
        topic = Topic.objects.get(name='coronavirus')
        self.assertEqual((topic.__str__()), topic.name)

    def test_post_str_method(self):
        """
        This test tests the post str method and verifies
        """
        post = Post.objects.get(pk='1')
        self.assertEqual((post.__str__()), post.title)

    def test_comment_str_method(self):
        """
        This test tests the comment str method and verifies
        """
        comment = Comment.objects.get(comment_body='Test comment body')
        self.assertEquals(str(comment), 'Comment Test comment body by userb')

    def test_post_upvote_defaults_to_zero(self):
        """
        This test tests the post default for upvote sets to zero and verifies
        """
        user_c = User.objects.create_user(
            username='userc', password='p3word')

        topic2 = Topic.objects.create(
            name='coronavirus1',
            slug='coronavirus1'
            )

        post2 = Post.objects.create(
            topic=topic2,
            title="Corona2",
            owner=user_c,
            slug="Corona2",
        )
        post2 = Post.objects.get(pk='2')
        self.assertEqual(post2.upvote, 0)
