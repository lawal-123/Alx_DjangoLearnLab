from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy

# --- Helper Functions for Role Checking ---

def is_admin(user):
    """Check if the user has the 'Admin' role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Check if the user has the 'Librarian' role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Check if the user has the 'Member' role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Role-Based Views ---

# The 'login_url' parameter directs unauthorized users to the login page.
# The files are named as requested (admin_view, librarian_view, member_view).

@user_passes_test(is_admin, login_url=reverse_lazy('login')) # Assuming 'login' is your login URL name
def admin_view(request):
    """Admin-only content."""
    return render(request, 'admin_view.html', {'role': 'Admin'})

@user_passes_test(is_librarian, login_url=reverse_lazy('login'))
def librarian_view(request):
    """Librarian-only content."""
    return render(request, 'librarian_view.html', {'role': 'Librarian'})

@user_passes_test(is_member, login_url=reverse_lazy('login'))
def member_view(request):
    """Member-only content."""
    return render(request, 'member_view.html', {'role': 'Member'})