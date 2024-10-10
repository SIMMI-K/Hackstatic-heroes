from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# # Create your models here.


# This signal will trigger whenever a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# This will save the UserProfile whenever the User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    user_profile, created = UserProfile.objects.get_or_create(user=instance)
    user_profile.save()
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

