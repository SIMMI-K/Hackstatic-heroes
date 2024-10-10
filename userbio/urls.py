from django.urls import path
from . import views
from .views import delete_userbio, userbio, edit_userbio


urlpatterns = [
    path('', views.userbio, name='userbio'),  # Display the user's profile and bookmarks
    path('edit/', views.edit_userbio, name='edit_userbio'),  # URL for editing user profile
    path('delete/', delete_userbio, name='delete_userbio'),
]
