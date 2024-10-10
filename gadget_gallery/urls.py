from django.contrib import admin
from django.urls import path, include
from blog.views import post_detail, post_list


# Alphabetical, empty ones at the end
urlpatterns = [
    path('accounts/', include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('userbio/', include('userbio.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),
]
