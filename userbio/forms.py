from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
        labels = {
            'bio': '',
        }
        
        # Add widgets to the form fields
        widgets = {
            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell us something about yourself...',
            }),
        }
