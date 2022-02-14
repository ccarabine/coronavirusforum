# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from .forms import PostForm, CommentForm


class TestPostForm(TestCase):

    def test_post_title_is_required(self):
        """
        This test tests the field "title" is  required
        checks
        1.form is not valid as title is blank
        2. There is a comment_body key in the dic
        3. There is an error message
        """
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_title_is_valid_with_data(self):
        """
        This test tests the field "title" is  required
        checks
        1. form is valid as title is contains characters
        """
        form = PostForm({'title': 'Corona Virus'})
        self.assertTrue(form.is_valid())

    def test_body_is_not_required(self):
        """
        This test tests the field "body" is not required
        checks
        1. form is valid as title is contains characters and no body field
        """
        form = PostForm({'title': 'title populated, empty body field'})
        self.assertTrue(form.is_valid())

    def test_postform_fields_are_explicit_in_form_metaclass(self):
        """
        This test tests the field in the meta only display
        checks
        1. The fields are in meta
        """
        form = PostForm()
        self.assertEqual(form.Meta.fields,
                         ('title', 'body', 'post_image', 'enable_voting'))


class TestCommentForm(TestCase):

    def test_comment_body_is_required(self):
        """
        This test tests the field "comment_body" is  required
        checks
        1. form is not valid as comment_body field is blank
        2. There is a comment_body key in the dic
        3. There is an error message
        """
        form = CommentForm({'comment_body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment_body', form.errors.keys())
        self.assertEqual(
            form.errors['comment_body'][0], 'This field is required.'
            )

    def test_comment_body_is_valid_with_data(self):
        """
        This test tests the field "comment_body" is  required
        checks
        1. form is valid as comment_body is contains characters
        """
        form = CommentForm({'comment_body': 'commentbody text'})
        self.assertTrue(form.is_valid())

    def test_commentform_fields_are_explicit_in_form_metaclass(self):
        """
        This test tests the field in the meta only display
        checks
        1. The field is in meta
        """
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ("comment_body",))
