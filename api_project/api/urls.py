# api/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookList,BookViewSet


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    # Maps GET requests to /api/books/ to the BookList view
    path('books/', BookList.as_view(), name='book-list'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
