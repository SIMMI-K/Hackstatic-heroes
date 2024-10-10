from django.conf import settings  # Ensure compatibility with custom user models later
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# # Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.user.username


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)  # Link to blog posts
    note = models.TextField(blank=True, null=True)  # A note specific to this bookmark
    created_on = models.DateTimeField(auto_now_add=True)  # Timestamp for when bookmark was added
    updated_on = models.DateTimeField(auto_now=True)  # Timestamp for when the bookmark or note was last updated

    def __str__(self):
        return f"{self.user.username}'s bookmark on {self.post.title}"

