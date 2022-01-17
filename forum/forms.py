from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import FormActions


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'body',
              'post_image', 'enable_voting')
    widgets = {
      'body': SummernoteWidget(), }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
  
    self.fields['title'].label = "Title"
    self.fields['post_image'].label = False
    
    self.fields['enable_voting'].label = "Enable voting"
    
    self.helper.layout = Layout(
       Field('title', placeholder='Make this interesting'),
       Field('body'),
       Row(
        Column(
          Field('post_image', placeholder='Image Upload')),
        Column('enable_voting', css_class="checkbox-lg "),
        FormActions(
          Submit('submit', 'Submit post',
                 css_class="btn btn-secondary")
          )
        ))
