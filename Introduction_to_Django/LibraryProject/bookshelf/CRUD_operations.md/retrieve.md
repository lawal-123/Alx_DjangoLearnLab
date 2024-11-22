<<<<<<< HEAD
from bookshelf.models import Book
book = Book.objects.get(title="1984")
books = Book.objects.all()
print(book)
for book in books:
    print(book)
=======
from bookshelf.models import Book
book = Book.objects.get(title="1984")
books = Book.objects.all()
print(book)
for book in books:
    print(book)
>>>>>>> 833a1e0c4ff758225723255cb9e94e655d996c89
