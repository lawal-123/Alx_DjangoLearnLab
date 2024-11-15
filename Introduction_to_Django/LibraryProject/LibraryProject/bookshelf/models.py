    # bookshelf/models.py
from django.db import models

class Book(models.Model):
    def __init__(self, title, author, publication_year)
        self.title = models.CharField(max_length=200)
        self.author = models.CharField(max_length=100)
        self.publication_year = models.IntegerField()

def __str__(self):
    return f"{self.title} by {self.author} ({self.publication_year})"
