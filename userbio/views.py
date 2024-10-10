from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages

# Create your views here.
@login_required  # Ensure that only logged-in users can view their profile
def userbio(request):
    # Check if the logged in user has a profile, amd create one if not
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user)
    
    # # Get the logged-in user's profile
    # user_profile = get_object_or_404(UserProfile, user=request.user)

    # Pass the profile and bookmarks to the template
    context = {
        'user_profile': user_profile,
    }

    return render(request, 'userbio/user_profile.html', context)


@login_required
def edit_userbio(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated sucessfully!')
            return redirect('userbio')  # Redirect back to the profile page
    else:
        form = UserProfileForm(instance=user_profile)
            
    return render(
        request, 'userbio/edit_user_profile.html', {'form': form})
    
    
@login_required
def delete_userbio(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        user_profile.delete()
        messages.success(request, 'Your profile has been deleted')
        return redirect('post_list')
    
    return render(request, 'userbio/confirm_delete.html', {
        'user_profile': user_profile})
