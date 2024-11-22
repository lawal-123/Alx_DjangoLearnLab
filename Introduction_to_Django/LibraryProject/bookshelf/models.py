<<<<<<< HEAD
    # bookshelf/models.py
from django.db import models

class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=100)
        publication_year = models.IntegerField()

def __str__(self):
    return f"{self.title} by {self.author} ({self.publication_year})"
=======
from django.db import models
class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=100)
        publication_year = models.IntegerField()

def __str__(self):
    return f"{self.title} by {self.author} ({self.publication_year})"
>>>>>>> 833a1e0c4ff758225723255cb9e94e655d996c89
