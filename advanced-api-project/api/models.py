from django.db import models
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200, help_text="The full name of the author.")

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a Book.
    Fields: title (string), publication_year (integer), and a Foreign Key to Author.
    
    Relationship Handling:
    The ForeignKey establishes a one-to-many relationship: one Author can have
    many Books. We use 'related_name="books"' on the ForeignKey so that we can
    access the list of a specific author's books using `author_instance.books.all()`.
    This is the key to nesting books under the AuthorSerializer.
    """
    title = models.CharField(max_length=255, help_text="The title of the book.")
    
    publication_year = models.IntegerField(
        help_text="The year the book was published (used for validation)."
    )
    
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books', # Key for nested serialization in AuthorSerializer
        help_text="The author of the book."
    )

    def __str__(self):
        return f"{self.title} by {self.author.name}"