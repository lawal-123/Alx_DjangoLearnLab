# relationship_app/models.py

from django.db import models

class Author(models.Model):
    """Represents the creator of books (One-to-Many target)."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Represents a book."""
    title = models.CharField(max_length=200)
    # One-to-Many relationship: One Author can have many Books.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Library(models.Model):
    """Represents a physical library building."""
    name = models.CharField(max_length=100)
    # Many-to-Many relationship: A Library can have many Books, and a Book 
    # can be in many Libraries.
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    """Represents the head librarian."""
    name = models.CharField(max_length=100)
    # One-to-One relationship: One Library has exactly one Librarian.
    library = models.OneToOneField(Library, on_delete=models.CASCADE, primary_key=True, related_name='librarian')

    def __str__(self):
        return self.name