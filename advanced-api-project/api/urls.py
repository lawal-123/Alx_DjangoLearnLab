"""
Step 2: Define URL Patterns

This module defines the routing for the 'api' application, connecting URL paths
to the generic views that handle CRUD operations for the Book model.
"""
from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    # List and Create Books:
    # URL: /api/books/
    # Methods: GET (List), POST (Create)
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),

    # Retrieve, Update, and Destroy a specific Book:
    # URL: /api/books/<int:pk>/
    # Methods: GET (Retrieve), PUT (Update), PATCH (Partial Update), DELETE (Destroy)
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail-update-destroy'),
]