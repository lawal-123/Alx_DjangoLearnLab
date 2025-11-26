from django.contrib import admin
# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

# --- Define the custom ModelAdmin for CustomUser ---

class CustomUserAdmin(BaseUserAdmin):
    # Fields that should be displayed in the change list view
    list_display = (
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'is_staff', 
        'date_of_birth' # Include custom field
    )

    # Fields that can be used to filter the list
    list_filter = (
        'is_staff', 
        'is_superuser', 
        'is_active', 
        'groups'
    )

    # Define the fields shown in the form when editing a user
    # We add a new fieldset for our custom fields
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Define the fields shown in the form when creating a user
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Fields to search by
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)


# Register your CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
