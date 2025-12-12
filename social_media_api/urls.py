# accounts/urls.py

from django.urls import path
from .views import RegistrationView, CustomAuthToken, ProfileView

urlpatterns = [
    # Route for User Registration (POST request)
    path('register/', RegistrationView.as_view(), name='register'),
    
    # Route for User Login (POST request)
    path('login/', CustomAuthToken.as_view(), name='login'),
    
    # Route for retrieving/updating the authenticated User's Profile (GET/PUT/PATCH request)
    path('profile/', ProfileView.as_view(), name='profile'),
]