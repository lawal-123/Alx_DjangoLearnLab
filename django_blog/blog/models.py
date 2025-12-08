from django.db import models
from django.contrib.auth.models import User
"Comment(models.Model)", "post", "created_at", "updated_at
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    # The Foreign Key relationship to Django's User model
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.title

    def __str__(self):
        return self.title
# Create your models here.
# blog/models.py (Update the Post model)
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager # New Import

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 🌟 New: TaggableManager provides the many-to-many relationship 🌟
    tags = TaggableManager() 
    # ... (rest of the Post model)
    
# ... (The Comment model remains unchanged)