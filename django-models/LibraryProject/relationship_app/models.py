from django.db import models

# 1. Author Model (The 'one' side of the ForeignKey relationship with Book)
class Author(models.Model):
   
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. Book Model (The 'many' side of the ForeignKey relationship with Author)
class Book(models.Model):
   
    title = models.CharField(max_length=200)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 3. Library Model (Contains a ManyToManyField to Book)
class Library(models.Model):
  
    name = models.CharField(max_length=150)

    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

# 4. Librarian Model (The 'one' side of the OneToOneField relationship with Library)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
from relationship_app.models import Author, Book, Library, Librarian
from django.db.models import Count # Imported but not used in these specific queries.

print("--- Starting Sample Queries Demonstration ---")

# --- 1. Data Setup ---
# Let's create some sample data so we have something to query.

# Authors (The 'One' in One-to-Many)
print("\n1. Creating Authors...")
author_a, created = Author.objects.get_or_create(name="Harper Lee")
author_b, created = Author.objects.get_or_create(name="J.R.R. Tolkien")
print(f"  Created Author A: {author_a.name}")
print(f"  Created Author B: {author_b.name}")

# Books (The 'Many' in One-to-Many, links to Author via ForeignKey)
print("\n2. Creating Books...")
book_1, created = Book.objects.get_or_create(title="To Kill a Mockingbird", author=author_a)
book_2, created = Book.objects.get_or_create(title="Go Set a Watchman", author=author_a)
book_3, created = Book.objects.get_or_create(title="The Hobbit", author=author_b)
book_4, created = Book.objects.get_or_create(title="The Lord of the Rings", author=author_b)
print(f"  Created Books: {book_1.title}, {book_2.title}, {book_3.title}, {book_4.title}")

# Libraries (The ManyToMany side)
print("\n3. Creating Libraries...")
library_a, created = Library.objects.get_or_create(name="Central City Library")
library_b, created = Library.objects.get_or_create(name="West Side Branch")
print(f"  Created Library A: {library_a.name}")
print(f"  Created Library B: {library_b.name}")

# Link Books to Libraries (Many-to-Many relationship setup)
# Library A stocks all books
library_a.books.set([book_1, book_2, book_3, book_4])
# Library B stocks only the Tolkien books
library_b.books.set([book_3, book_4])
print("  Books assigned to Libraries.")

# Librarians (The 'One' in One-to-One, links to Library via OneToOneField)
print("\n4. Creating Librarians...")
librarian_a, created = Librarian.objects.get_or_create(name="Ms. Eleanor Vance", library=library_a)
librarian_b, created = Librarian.objects.get_or_create(name="Mr. David Smith", library=library_b)
print(f"  Created Librarians: {librarian_a.name}, {librarian_b.name}")


# --- 2. Sample Queries ---

# 1. Query all books by a specific author (ForeignKey reverse lookup)
print("\n--- QUERY 1: Books by a Specific Author (Harper Lee) ---")

harper_lee_books = author_a.book_set.all()
print(f"Books by {author_a.name}:")
for book in harper_lee_books:
    print(f"- {book.title}")


# 2. List all books in a library (ManyToMany field traversal)
print("\n--- QUERY 2: All Books in Central City Library ---")
# Access the 'books' ManyToMany field directly on the Library instance.
library_a_books = library_a.books.all()
print(f"Books stocked at {library_a.name}:")
for book in library_a_books:
    print(f"- {book.title}")


# 3. Retrieve the librarian for a library (OneToOneField reverse lookup)
print("\n--- QUERY 3: Find the Librarian for West Side Branch ---")
try:
    librarian = library_b.librarian
    print(f"The Librarian for {library_b.name} is: {librarian.name}")
except Librarian.DoesNotExist:
    # This block handles the case where a Library might exist without a Librarian.
    print(f"No Librarian found for {library_b.name}.")

print("\n--- Queries Demonstration Complete ---")    