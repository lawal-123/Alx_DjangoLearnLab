# relationship_app/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
# --- FIX: Ensure Library model is imported ---
from .models import Book, Library 

# --- Function-based View ---
# ... (list_all_books function remains the same)

# --- Class-based View (DetailView) ---

class LibraryDetailView(DetailView):
    """
    Displays details for a specific Library, including all books associated 
    via the ManyToManyField.
    """
    # Model to query - Requires the 'Library' model to be imported.
    model = Library 
    
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.prefetch_related(
            'books__author'
        )