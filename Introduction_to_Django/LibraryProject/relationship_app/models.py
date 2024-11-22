<<<<<<< HEAD
from django.db import models

# Create your models here.
=======
from django.db import models
from django.db import models
class Author(models.model):
    name = models.charfield(max_length=150)
    
    def_str_(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return self.title
    
class Library(modles.model):
    class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name
# Create your models here.
>>>>>>> 833a1e0c4ff758225723255cb9e94e655d996c89
