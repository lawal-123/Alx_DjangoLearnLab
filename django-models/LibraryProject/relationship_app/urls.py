# relationship_app/urls.py

from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    # 1. Function-based view URL (e.g., /app/books/)
    path('books/', views.list_all_books, name='list_all_books'),
    
    # 2. Class-based view URL (e.g., /app/library/1/)
    # The <int:pk> captures the primary key (ID) of the Library object 
    # to be displayed.
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]