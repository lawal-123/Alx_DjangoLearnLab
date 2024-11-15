class Book:
    def __init__(self, title, author, publication_year):
        # Ensure the title is a string with a maximum length of 200 characters
        if len(title) > 200:
            raise ValueError("Title cannot be longer than 200 characters.")
        self.title = title
        
        # Ensure the author is a string with a maximum length of 100 characters
        if len(author) > 100:
            raise ValueError("Author name cannot be longer than 100 characters.")
        self.author = author
        
        # Ensure the publication year is an integer
        if not isinstance(publication_year, int):
            raise ValueError("Publication year must be an integer.")
        self.publication_year = publication_year

    def __str__(self):
        """Return a string representation of the book."""
        return f"'{self.title}' by {self.author}, published in {self.publication_year}"
print(book)
