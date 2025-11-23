from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    # Choices for the user role
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signal to automatically create a UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Ensure the profile exists before trying to save it
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        # If the profile doesn't exist (e.g., if a user was created without the signal running), 
        # this will create it, though the 'create_user_profile' should handle it.
        UserProfile.objects.create(user=instance)
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    # Include other fields as needed

    class Meta:
        # Define the custom permissions here
        permissions = [
            ("can_add_book", "Can add new books to the inventory"),
            ("can_change_book", "Can modify existing book details"),
            ("can_delete_book", "Can remove books from the inventory"),
        ]
        verbose_name = "Book Entry"
        verbose_name_plural = "Book Entries"

    def __str__(self):
        return self.title

# REMEMBER to run 'python manage.py makemigrations relationship_app' 
# and 'python manage.py migrate' after this change.