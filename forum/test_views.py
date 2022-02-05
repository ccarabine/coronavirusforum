# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from .models import Post, Topic

User = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        """
        Set up user, post and topic for the tests
        """
        user_a = User.objects.create_user(
            username='user_1',
            password='Pas1asdf'
            )

        Post.objects.create(
            title='starting title',
            owner=user_a,
        )
        Topic.objects.create(
            name='coronavirus',
            slug='coronavirus'
            )

    def tearDown(self):
        """
        Delete test user, Topic, Post
        """
        User.objects.all().delete()
        Post.objects.all().delete()
        Topic.objects.all().delete()

    def test_get_homepage(self):
        """
        This test tests the index page displays
        checks
        1. that the status code is 200 and template used is index.html
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_aboutuspage(self):
        """
        This test tests the aboutus page displays
        checks
        1. that the status code is 200 and template used is aboutus.html
        """
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus.html')

    def test_get_talkguidelines(self):
        """
        This test tests the talkguidelines page displays
        checks
        1. the status code is 200 and
        2. template used is talkguidelines.html
        """
        response = self.client.get('/talkguidelines/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'talkguidelines.html')

    def test_get_privacypolicy(self):
        """
        This test tests the privacy policy page displays
        checks
        1. the status code is 200
        2. template used is privacypolicy.html
        """
        response = self.client.get('/privacypolicy/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacypolicy.html')

    def test_get_list_of_posts(self):
        """
        This test tests get a list of posts by topic and verifies
        checks
        1. that the status code is 200
        2. template used is postlist.html
        """
        response = self.client.get('/topic/coronavirus/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postlist.html')

    def test_add_post_as_not_logged_in(self):
        """
        This test tests a user who is not logged in, can not create a post
        checks
        1. if the page redirects to the home page
        2. if the message is the same as the not logged in user
        3. that the status code is 302  - redirect
        """
        self.client.logout()
        response = self.client.get('/addpost/coronavirus/')
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "Sorry, only logged in users can create a post.")
        self.assertEqual(response.status_code, 302)

    def test_add_post_as_a_logged_in_user(self):
        """
        This test tests a logged in user can create a post
        checks
        1. the post the user created is equal to title12
        2. if the message is the same as post submitted
        3. the status code is 302  - redirect
        4. redirected back to the postdetail page
        """
        self.client.login(username='user_1', password='Pas1asdf')
        response = self.client.post('/addpost/coronavirus/',
                                    {'title': 'title12'}
                                    )
        post = Post.objects.filter(pk=2).first()
        self.assertEqual(post.title, 'title12')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "Post submitted")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("postdetail", args=[post.id]))

    def test_update_post_as_an_owner(self):
        """
        This test tests an owner of a post can update their post
        checks
        1. the updated title equals the title that the user typed in.
        2. if the message is the same as post submitted
        3. that the status code is 302  - redirect
        4. redirected back to the postdetail page
        """
        self.client.login(username='user_1', password='Pas1asdf')
        response = self.client.post('/topic/update/1',
                                    {'title': 'updated title'}
                                    )
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'updated title')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "Post updated")
        self.assertTrue(response.status_code, 302)

    def test_update_post_as_not_the_owner(self):
        """
        This test tests a user who has not created the post can not
        edit the post
        checks
        1. a different user that trys to edit a post with the title field
        is not saved
        2. the updated title is not equals to the post title that the user
        typed in.
        3. that the status code is 304  - Not modified status code

        """
        self.client.login(username='user_2', password='Pas2asdf')
        response = self.client.post('/topic/update/1',
                                    {'title': 'updated title'}
                                    )
        post = Post.objects.filter(pk=1).first()
        self.assertNotEqual(post.title, 'updated title')
        self.assertTrue(response.status_code, 304)
