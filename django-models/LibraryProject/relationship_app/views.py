# relationship_app/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
# Assuming your models are defined in .models
from .models import Book, Library 

### Function-based View (FBV): List all Books ###

def book_list_view(request):
    """
    Lists all books from the database and renders them using list_books.html.
    """
    # Query all Book objects
    all_books = Book.objects.all()
    
    # Context to pass to the template
    context = {
        'books': all_books
    }
    
    # Render the template
    return render(request, 'relationship_app/list_books.html', context)


### Class-based View (CBV): Library Detail ###

class LibraryDetailView(DetailView):
    """
    Displays details for a specific Library, including all books in it.
    Uses Django's DetailView.
    """
    # 1. Specify the model to use for the primary object
    model = Library
    
    # 2. Specify the template file to render
    template_name = 'relationship_app/library_detail.html'
    
    # 3. Specify the context variable name (optional, defaults to 'object' or 'library')
    context_object_name = 'library' 
    
    # DetailView automatically fetches the object based on the primary key 
    # passed in the URL (typically 'pk').
    
    # Note: The template uses {{ library.books.all }} to access the related books 
    # based on the model's reverse relationship.