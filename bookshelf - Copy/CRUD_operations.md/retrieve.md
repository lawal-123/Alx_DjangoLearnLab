from bookshelf.models import Book
book = Book.objects.get(title="1984")
books = Book.objects.all()
print(book)
for book in books:
    print(book)
