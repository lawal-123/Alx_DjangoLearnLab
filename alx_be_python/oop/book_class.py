class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __del__(self):
        print(f"deleting {self.title} upon object deletion")
    def __repr__(self):
        return f"(book:'{self.title}', '{self.author}','{self.year}')"

from book_class import Book
def main():   
    my_book = Book("1984", "george orwell", 1949)
    def __str__(self):
        print(my_book)
    def __repr__(self):
        print(repr(my_book))
    def __del__(self):
        del my_book   
if __name__ == "__main__":
    main()