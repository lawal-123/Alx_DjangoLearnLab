from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()

def __str__(self):
    return self.title

class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifier for authentication
    instead of usernames. It inherits from BaseUserManager to handle the
    creation logic.
    """
    def create_user(self, username, email, password, **extra_fields):
        """
        Create and save a User with the given username, email, and password.
        The added fields date_of_birth and profile_photo are handled via
        extra_fields.
        """
        if not username:
            raise ValueError(_('The Username field must be set'))
        if not email:
            raise ValueError(_('The Email field must be set'))

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given username, email, and password.
        Superusers must have is_staff=True and is_superuser=True.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        # Default values for new fields if not provided during superuser creation
        extra_fields.setdefault('date_of_birth', '1900-01-01')

        return self.create_user(username, email, password, **extra_fields)


# --- Custom User Model ---

class CustomUser(AbstractUser):
    """
    Custom User model extending Django's built-in AbstractUser.
    It adds 'date_of_birth' and 'profile_photo' fields.
    """
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

    # You can customize the USERNAME_FIELD and REQUIRED_FIELDS here,
    # but by default, AbstractUser uses 'username' and requires 'email'.
    # Example to change to email-based login:
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username