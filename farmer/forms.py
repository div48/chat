from django import forms
from .models import *
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ('image','image_caption', 'tag_someone',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
      attrs={
        'class': 'form-control',
        'placeholder': 'Comment here !',
        'rows': 4,
        'cols': 50
      }))

    class Meta:
      model = Comment
      fields = ['content']