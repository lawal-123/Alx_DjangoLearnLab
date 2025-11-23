# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
# --- 🛑 FIX THIS IMPORT 🛑 ---
from .models import  Library 

### Function-based View (FBV): List all Books ###

def book_list_view(request):
    """
    Lists all books from the database and renders them using list_books.html.
    """
    all_books = Book.objects.all()
    
    context = {
        'books': all_books
    }
    
    return render(request, 'relationship_app/list_books.html', context)


### Class-based View (CBV): Library Detail ###

class LibraryDetailView(DetailView):
    """
    Displays details for a specific Library, including all books in it.
    Uses Django's DetailView.
    """
    # This requires the 'Library' model to be imported above.
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'