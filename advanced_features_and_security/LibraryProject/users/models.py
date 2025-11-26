# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
# ... other imports

class CustomUser(AbstractUser):
    # ... your date_of_birth and profile_photo fields ...

    # OVERRIDE the fields from AbstractUser to prevent reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="custom_user_set", # <--- ADDED related_name
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="custom_user_permissions_set", # <--- ADDED related_name
        related_query_name="custom_user",
    )
    # ... rest of your model ...