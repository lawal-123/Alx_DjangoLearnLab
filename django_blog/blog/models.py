from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    # The Foreign Key relationship to Django's User model
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    
<<<<<<< HEAD
    def __str__(self):
        return self.title

=======
>>>>>>> 58c13a133595431a9a850425bcafab54a570ebfa
    def __str__(self):
        return self.title
