from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'body',)
        # This removes the label
        labels = {
            'body': '',
        }
