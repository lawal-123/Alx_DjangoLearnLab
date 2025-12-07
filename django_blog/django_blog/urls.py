# blog/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from . import views

urlpatterns = [
    # ... your existing blog paths (e.g., path('', views.home, name='blog-home'))
    
    # Custom Registration View
    path('register/', views.register, name='register'),
    
    # Custom Profile View (requires login)
    path('profile/', views.profile, name='profile'), 
    
    # Built-in Login View
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    
    # Built-in Logout View
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'), 
]