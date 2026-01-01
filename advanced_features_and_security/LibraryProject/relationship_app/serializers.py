from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone
import datetime

# --- Step 4 & 5: Create Custom Serializers with Validation and Documentation ---

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    It serializes the title, publication year, and the author's primary key (for write operations).
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['id']

    # --- Custom Validation Implementation (Step 4) ---
    def validate_publication_year(self, value):
        """
        Ensures the publication year is not in the future.
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    It demonstrates nested serialization by including the related 'books'.
    """
    # Nested Serialization: Use the BookSerializer to display a list of all 
    # books associated with this author instance.
    # 'many=True' indicates it's a list (queryset) of related objects.
    # 'read_only=True' ensures books cannot be created/updated via the Author endpoint.
    # The source='books' refers to the related_name defined on the ForeignKey in Book model.
    books = BookSerializer(many=True, read_only=True, source='books') 

    class Meta:
        model = Authorp
        fields = ['id', 'name', 'books'] # Include 'books' for the nested output
        read_only_fields = ['id']