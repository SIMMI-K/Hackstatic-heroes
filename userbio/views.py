from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Bookmark

# Create your views here.
@login_required  # Ensure that only logged-in users can view their profile
def userbio(request):
    # Check if the logged in user has a profile, amd create one if not
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # # Get the logged-in user's profile
    # user_profile = get_object_or_404(UserProfile, user=request.user)

    # Get the user's bookmarks
    user_bookmarks = Bookmark.objects.filter(user=request.user)

    # Pass the profile and bookmarks to the template
    context = {
        'user_profile': user_profile,
        'user_bookmarks': user_bookmarks,
    }

    return render(request, 'userbio/user_profile.html', context)
