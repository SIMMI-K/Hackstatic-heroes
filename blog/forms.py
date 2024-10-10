from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'slug']

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'body',)
        # This removes the label
        labels = {
            'body': '',
        }