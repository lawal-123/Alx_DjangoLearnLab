# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm # Used for profile editing
from django.contrib import messages
from .forms import BlogUserCreationForm # Our custom form

# ----------------- Registration View -----------------

def register(request):
    if request.method == 'POST':
        form = BlogUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optional: Log the user in immediately after registration
            # from django.contrib.auth import login
            # login(request, user)
            messages.success(request, f'Account created for {user.username}! You can now log in.')
            return redirect('login') # Redirect to the login page
    else:
        form = BlogUserCreationForm()
        
    return render(request, 'blog/register.html', {'form': form})

# ----------------- Profile Management View -----------------

# The @login_required decorator ensures only logged-in users can access this page
@login_required
def profile(request):
    # UserChangeForm allows viewing/editing the built-in User model fields
    if request.method == 'POST':
        # Pass the current user instance to the form for modification
        form = UserChangeForm(request.POST, instance=request.user) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile') # Redirect to refresh the profile page
    else:
        form = UserChangeForm(instance=request.user)
        
    return render(request, 'blog/profile.html', {'form': form})