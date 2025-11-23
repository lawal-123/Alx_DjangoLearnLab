# relationship_app/urls.py

from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    # URL for Function-based View (FBV)
    # Accessible via: /relationship/books/
    path('books/', views.book_list_view, name='book-list'),
    
    # URL for Class-based View (CBV)
    # Accessible via: /relationship/library/1/ (where 1 is the primary key)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]

# Don't forget to include this app's urls.py in your main project's urls.py 
# (e.g., path('relationship/', include('relationship_app.urls')) )