# relationship_app/urls.py

# relationship_app/urls.py

from django.urls import path
from .views import LibraryDetailView
# ... other imports ...

urlpatterns = [
    # ... FBV URL ...
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]