from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the author.")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the book.")
    publication_year = models.IntegerField(help_text="Year the book was published.")
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE, help_text="Author of the book.")

    def __str__(self):
        return self.title

from django.db import models

class Author(models.Model):
    """
    Represents an author in the system.

    Fields:
        name: A CharField to store the name of the author.
    
    Relationships:
        - An Author can have multiple Books. This is a one-to-many relationship where
          one Author can be associated with many Book instances.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book written by an Author.

    Fields:
        title: A CharField to store the title of the book.
        publication_year: A PositiveIntegerField to store the publication year of the book.
        author: A ForeignKey that establishes the relationship between Book and Author.

    Relationships:
        - A Book is associated with a single Author, making it a many-to-one relationship.
    """
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
