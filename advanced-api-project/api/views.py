from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Apply permissions based on the action (HTTP method)
    def get_permissions(self):
        # Allow Read access (GET) to any user
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        # Restrict Write access (POST) to authenticated users only
        return [permissions.IsAuthenticated()]

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles:
    - GET /api/books/<int:pk>/ (Retrieve a single book) - DetailView
    - PUT /api/books/<int:pk>/ (Update an existing book) - UpdateView
    - PATCH /api/books/<int:pk>/ (Partial Update) - UpdateView
    - DELETE /api/books/<int:pk>/ (Delete a book) - DeleteView

    Customization (Permissions):
    - GET request uses AllowAny (read-only access for everyone).
    - PUT/PATCH/DELETE requests use IsAuthenticated (only logged-in users can modify/delete).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Apply permissions based on the action (HTTP method)
    def get_permissions(self):
        # Allow Read access (GET) to any user
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        # Restrict Write/Delete access (PUT/PATCH/DELETE) to authenticated users only
        return [permissions.IsAuthenticated()]
# Create your views here.
