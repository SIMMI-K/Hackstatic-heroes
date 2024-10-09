# from django.conf import settings  # Ensure compatibility with Allauth later
# from django.db import models
# from cloudinary.models import CloudinaryField

# # Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     bio = modelsTextField(blank=True, null=True)
#     profile_picture = models.CharField  # TODO This will be cloudinary when someone has installed it
#     bookmarks = models.ManyToManyField('BlogPost', related_name='bookmarked_by', blank=True)
    
#     def __str__(self):
#         return self.user.username
    
    