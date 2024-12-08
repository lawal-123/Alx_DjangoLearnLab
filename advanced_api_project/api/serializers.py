from rest_framework import serializers
from .models import Author, Book

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        from datetime import date
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to serialize related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

NOTES:



from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    
    This serializer handles the serialization of all fields in the Book model.
    
    Custom Validation:
        - Ensures the `publication_year` field is not set to a future year.
    """
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields of the Book model

    def validate_publication_year(self, value):
        """
        Custom validation to ensure that the publication year is not in the future.
        """
        from datetime import date
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    This serializer handles the serialization of the `name` field of the Author model
    and includes a nested `BookSerializer` to serialize the related books.

    Nested Serialization:
        - A list of books associated with the author is serialized using the `BookSerializer`.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']  # Serialize the name field and the related books
