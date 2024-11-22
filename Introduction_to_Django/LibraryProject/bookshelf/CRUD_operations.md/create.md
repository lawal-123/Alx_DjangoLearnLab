<<<<<<< HEAD

# Create Book Instance
 Command:
python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
=======

# Create Book Instance
 Command:
python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
>>>>>>> 833a1e0c4ff758225723255cb9e94e655d996c89
print(book)