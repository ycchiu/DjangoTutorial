from django import forms

from .models import Link

class PostForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('title_text', 'url')