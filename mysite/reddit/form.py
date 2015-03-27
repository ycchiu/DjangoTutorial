from django import forms

from .models import Link, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('title_text', 'url')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content_text')