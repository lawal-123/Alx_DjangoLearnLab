# relationship_app/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# --- Function-based View ---

def list_all_books(request):
    """
    Lists all Book objects in the database and renders them using a template.
    This view demonstrates a simple list query (Book.objects.all()).
    """
    # Query all books, ordering by title
    all_books = Book.objects.select_related('author').order_by('title')
    
    context = {
        'books': all_books
    }
    
    # Renders the HTML template list_books.html
    return render(request, 'relationship_app/list_books.html', context)


# --- Class-based View (DetailView) ---

class LibraryDetailView(DetailView):
    """
    Displays details for a specific Library, including all books associated 
    via the ManyToManyField.
    This view demonstrates retrieving a single object and accessing its 
    ManyToManyField relationship (library.books.all()).
    """
    # Model to query
    model = Library
    
    # Template to use
    template_name = 'relationship_app/library_detail.html'
    
    # The URL pattern will use 'pk' (primary key) to look up the library object
    context_object_name = 'library'

    # Optimization: Use select_related/prefetch_related for associated data.
    # Since 'books' is ManyToMany, we use prefetch_related.
    # We also prefetch the author for each book to avoid N+1 queries in the template.
    def get_queryset(self):
        return Library.objects.prefetch_related(
            'books__author'
        )
