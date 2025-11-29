# api/views.py

from rest_framework import generics
# Import the Book model
from bookshelf.models import Book
# Import the newly created serializer
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API endpoint that allows listing all Book instances.
    It provides read-only access to the list of books.
    """
    # 1. Define the queryset: Which records to retrieve (all books)
    queryset = Book.objects.all()
    
    # 2. Define the serializer_class: How to format the retrieved data
    serializer_class = BookSerializer

    # Optional: Configure permissions for read-only access (Good security practice)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]