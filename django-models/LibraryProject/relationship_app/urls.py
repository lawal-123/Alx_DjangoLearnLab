# relationship_app/urls.py

from django.urls import path
from . import views
from .views import LibraryDetailView # Keep existing imports

# Import Django's built-in views for authentication
from django.contrib.auth.views import LoginView, LogoutView 

urlpatterns = [
    # Existing App URLs
    path('books/', views.book_list_view, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    
    # --- Authentication URLs ---
    
    # Registration (Custom FBV)
    path('register/', views.register_view, name='register'),
    
    # Login (Built-in Class-based View)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Logout (Built-in Class-based View)
    # The default behavior is to log out and redirect to LOGOUT_REDIRECT_URL
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]