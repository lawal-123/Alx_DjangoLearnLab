# relationship_app/query_samples.py

# NOTE: This script is intended to be run inside the Django shell:
# $ python manage.py shell

# Import the models we need
from relationship_app.models import Author, Book, Library, Librarian
from django.db.models import Count # Useful for more complex queries

## --- 1. Data Setup (Only run this once in the shell) ---

def setup_data():
    """Creates sample data for demonstration."""
    
    # 1. Authors and Books (One-to-Many)
    tolkien, created = Author.objects.get_or_create(name='J.R.R. Tolkien')
    rowling, created = Author.objects.get_or_create(name='J.K. Rowling')

    hobbit, created = Book.objects.get_or_create(title='The Hobbit', author=tolkien)
    lotr, created = Book.objects.get_or_create(title='The Lord of the Rings', author=tolkien)
    stone, created = Book.objects.get_or_create(title='Philosopher\'s Stone', author=rowling)

    # 2. Library and Librarian (One-to-One)
    central_lib, created = Library.objects.get_or_create(name='Central City Library')
    
    # 3. Add Librarian (One-to-One)
    librarian, created = Librarian.objects.get_or_create(name='Ms. Eleanor Vance', library=central_lib)
    
    # 4. Library Books (Many-to-Many)
    # Add books to the Central City Library's collection
    central_lib.books.add(hobbit, lotr, stone)
    
    print("\n✅ Sample data created successfully.")

# Run the setup function if you are testing this in a fresh shell
# setup_data() 

## --- 2. Relationship Queries ---

def run_queries():
    """Executes the specific queries requested."""
    print("\n--- Running Django ORM Queries ---")
    
    # ----------------------------------------------------------------------

    ## 1. Query all books by a specific author. (One-to-Many)
    # We use the 'related_name' ('books') defined on the ForeignKey in the Book model.
    try:
        author_name = 'J.R.R. Tolkien'
        author_obj = Author.objects.get(name=author_name)
        
        # Accessing the related books directly
        books_by_author = author_obj.books.all() 
        
        print(f"\n📚 Books by {author_name}:")
        if books_by_author.exists():
            for book in books_by_author:
                print(f"  - {book.title}")
        else:
            print("  - No books found.")
            
    except Author.DoesNotExist:
        print(f"\nAuthor '{author_name}' not found.")
        
    print("-" * 40)

    # ----------------------------------------------------------------------

    ## 2. List all books in a library. (Many-to-Many)
    # We use the ManyToManyField 'books' defined on the Library model.
    try:
        library_name = 'Central City Library'
        library_obj = Library.objects.get(name=library_name)
        
        # Accessing the related books directly
        books_in_library = library_obj.books.all().order_by('title')
        
        print(f"\n📖 Books in {library_name}:")
        if books_in_library.exists():
            for book in books_in_library:
                print(f"  - {book.title} (Author: {book.author.name})")
        else:
            print("  - Library collection is empty.")
            
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")
        
    print("-" * 40)
    
    # ----------------------------------------------------------------------

    ## 3. Retrieve the librarian for a library. (One-to-One)
    # We use the 'related_name' ('librarian') defined on the OneToOneField in the Librarian model.
    try:
        library_name = 'Central City Library'
        library_obj = Library.objects.get(name=library_name)
        
        # Accessing the related librarian directly
        librarian_obj = library_obj.librarian
        
        print(f"\n👩‍💼 Librarian for {library_name}:")
        print(f"  - {librarian_obj.name}")
            
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian is currently assigned to '{library_name}'.")

    print("\n--- Queries Complete ---")

# Example of how to call the functions in the shell:
# setup_data()
# run_queries()