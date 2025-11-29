# api/views.py

from rest_framework import generics, viewsets, permissions
from bookshelf.models import Book
from .serializers import BookSerializer

# ... BookList definition ...

# --- Step 3: Define Permission Classes for ViewSet ---
class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Books, secured with Token Authentication and custom permissions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # SECURITY: Define the base permission class for the whole ViewSet
    # This setting requires authentication for *all* methods by default.
    permission_classes = [permissions.IsAuthenticated] 

    # SECURITY: Use a dictionary to override permissions for specific actions (methods).
    # This is standard practice for role-based access control.
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        # Read-only actions (GET/HEAD/OPTIONS)
        if self.action in ['list', 'retrieve']:
            # Allows authenticated users to view the list and details
            return [permissions.IsAuthenticated()] 
        
        # Write actions (POST/PUT/PATCH/DELETE)
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            # RESTRICTS write access to only Admin users (e.g., staff/superusers)
            return [permissions.IsAdminUser()]
        
        return super().get_permissions()