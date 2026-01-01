from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        """Set up test data and users."""
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984", 
            author=self.author, 
            publication_year=1949
        )
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        # Assuming detail, update, and delete use 'pk'
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    # --- CRUD Tests ---

    def test_get_all_books(self):
        """Test retrieving the list of books (Public)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        """Test creating a book as an authenticated user."""
        self.client.login(username='testuser', password='password123')
        data = {"title": "Animal Farm", "author": self.author.id, "publication_year": 1945}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Test updating a book's title."""
        self.client.login(username='testuser', password='password123')
        data = {"title": "Nineteen Eighty-Four"}
        # patch allows partial updates
        response = self.client.patch(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # --- Permissions Tests ---

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create books."""
        data = {"title": "Forbidden Book", "author": self.author.id, "publication_year": 2024}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- Advanced Query Tests (Filtering/Searching) ---

    def test_filter_books_by_title(self):
        """Test filtering by title query parameter."""
        response = self.client.get(self.list_url, {'title': '1984'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "1984")

    def test_search_books(self):
        """Test searching functionality."""
        response = self.client.get(f"{self.list_url}?search=Orwell")
        self.assertEqual(len(response.data), 1)