class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class Ebook(Book):
    def __init__(self, title, author, file_size):
        super(). __init__(title, author)
        self.file_size = file_size
class Printbook(Book):
    def __init__(self, title, author, page_count):
        super(). __init__(title, author)
        self.page_count = page_count
class Library:
    def __init__(self):
        self.books = []
        def add_book(self, book):
            self.books.append(book)
        def list_books(self):
            for book in self.books:
                print(f"{book.title} by {book.author}")
from library_system import Book, EBook, PrintBook, Library
def main():
    my_Libraary  = Library()
    classic_book = Book("price and judice", "jane austen")
    digital_novel = Ebook("digital fortress", "dan brown", 500)
    paper_novel = Printbook("The catcher in the rye", "j.d. salinger", 234)

# Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()
if __name__ == "__main__":
    main()