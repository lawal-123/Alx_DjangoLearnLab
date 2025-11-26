from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# --- Custom User Manager (Implemented in Step 3) ---

class CustomUserManager(BaseUserManager):
    """
    Custom user manager to handle user creation for the CustomUser model.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a regular User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        # Superuser creation requires 'date_of_birth' and 'profile_photo'
        # depending on your form/application logic. 
        # For simplicity in the terminal, we can provide defaults or 
        # assume they will be set later. 
        # For terminal use, 'date_of_birth' and 'profile_photo' 
        # may not be required during create_superuser call if they 
        # have null=True/blank=True, but let's ensure the user sets them 
        # if they are required.
        
        # Note: By default, AbstractUser requires 'username'. If you want 
        # to use 'email' as the primary identifier, you should set 
        # USERNAME_FIELD = 'email' in your CustomUser model. 
        # We'll stick to AbstractUser's defaults and ensure a username is passed.
        
        return self.create_user(email, password, **extra_fields)

# --- Custom User Model (Implemented in Step 1) ---

class CustomUser(AbstractUser):
    # Set email as the unique identifier instead of username
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username'] # Required when creating a user via createsuperuser

    # Custom Fields
    date_of_birth = models.DateField(
        null=True, 
        blank=True, 
        verbose_name=_('Date of Birth')
    )
    profile_photo = models.ImageField(
        upload_to='profile_photos/', 
        null=True, 
        blank=True, 
        verbose_name=_('Profile Photo')
    )

    # Use the custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.email or self.username

    # If Book is defined later in the file, use the string reference:
    # book = models.ForeignKey('Book', on_delete=models.CASCADE) 

    # If the model was renamed, e.g., to BookItem:
    # book = models.ForeignKey('BookItem', on_delete=models.CASCADE)# relationship_app/models.py
class BookLoan(models.Model):
    # ...
    # Use 'Book' as a string literal
    book = models.ForeignKey('Book', on_delete=models.CASCADE)