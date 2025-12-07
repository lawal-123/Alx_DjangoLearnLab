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
# blog/urls.py (Update your existing file)
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views # Assuming your custom views (register, profile) are still here

urlpatterns = [
    # ------------------ Blog Posts (CRUD) ------------------
    # R (List) - Accessible to all
    path('', views.PostListView.as_view(), name='blog-home'),
    
    # C (Create) - Requires Login
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    
    # R (Detail) - Accessible to all
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    
    # U (Update) - Requires Login and Author check
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    
    # D (Delete) - Requires Login and Author check
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    
    # ------------------ Authentication (Existing Paths) ------------------
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'), 
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'), 
]
# blog/urls.py (Add these paths to your existing file)
from . import views 
# ... (Your existing urlpatterns)

urlpatterns = [
    # ... (Existing Post CRUD URLS, e.g., path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'), )

    # ------------------ Comment URLs ------------------
    # C (Create Comment) - Linked to a specific Post PK
    path('post/<int:post_pk>/comment/new/', views.CommentCreateView.as_view(), name='comment-create'),
    
    # U (Update Comment) - Linked to a specific Comment PK
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    
    # D (Delete Comment) - Linked to a specific Comment PK
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]