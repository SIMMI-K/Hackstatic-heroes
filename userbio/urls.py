from django.urls import path
from . import views

urlpatterns = [
    path('', views.userbio, name='userbio'),  # Display the user's profile and bookmarks
]
