from django import forms
from .models import MediaItem, Comment

class MediaItemForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ['title', 'description', 'file', 'media_type', 'category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']