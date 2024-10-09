from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

