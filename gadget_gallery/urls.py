from django.contrib import admin
from django.urls import path, include



# Alphabetical, empty ones at the end
urlpatterns = [
    path('accounts/', include("allauth.urls")),
    path('admin/', admin.site.urls),
    # path('userbio/', userbio.urls, name='userbio-urls'),
    path('summernote/', include('django_summernote.urls')),
    path("blog/", include("blog.urls"), name="blog-urls"),

]

