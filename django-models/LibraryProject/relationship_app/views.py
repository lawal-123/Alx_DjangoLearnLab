# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login # Import the login function

# ... (Keep your existing views: book_list_view, LibraryDetailView) ...

# --- Registration View ---
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user
            user = form.save()
            # Log the user in immediately after registration
            login(request, user) 
            # Redirect to a desired page (e.g., the book list)
            return redirect('book-list') 
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    # Renders the provided register.html template
    return render(request, 'relationship_app/register.html', context)