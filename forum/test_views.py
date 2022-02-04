# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase
from django.contrib.auth import get_user_model
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from .models import Post

User = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        """
        Create test user(regular and super user), topic
         """
        """
        Set up users for the tests
        """
        admin = User.objects.create_superuser(
            username='admin', password='Pasad1232')

        user_a = User.objects.create_user(
            username='user_1',
            password='Pas1asdf'
            )
        
        user_b = User.objects.create_user(
            username='user_2',
            password='Pas2asdf'
            )
        
        Post.objects.create(
            title='starting title',
            owner=user_a,
        )

    def tearDown(self):
        """
        Delete test user, Topic, Post
        """
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_get_homepage(self):
        """
        This test tests the index page displays
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_get_aboutuspage(self):
        """
        This test tests the aboutus page displays
        """
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus.html')
    
    def test_get_talkguidelines(self):
        """
        This test tests the talkguidelines page displays
        """
        response = self.client.get('/talkguidelines/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'talkguidelines.html')
        
    def test_get_privacypolicy(self):
        """
        This test tests the privacy policy page displays
        """
        response = self.client.get('/privacypolicy/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacypolicy.html')
