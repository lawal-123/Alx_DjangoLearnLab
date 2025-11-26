from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

# --- Custom Admin Class ---

class CustomUserAdmin(BaseUserAdmin):
    """
    Custom Admin class for CustomUser.
    This modifies the fields displayed in the admin change form and the list view.
    """
    # Fields displayed in the list view (table)
    list_display = (
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'is_staff', 
        'date_of_birth' # Added field
    )

    # Fields to display in the user change form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name', 
                'last_name', 
                'email', 
                'date_of_birth',  # Added field
                'profile_photo'   # Added field
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active', 
                'is_staff', 
                'is_superuser',
                'groups', 
                'user_permissions'
            ),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields that can be edited in the list view (optional)
    list_editable = ['is_staff', 'date_of_birth'] 

# Unregister the default User model if your app has the CustomUser model
# If the app containing CustomUser is not the app where the default User model
# was registered, you may not need the unregister step.

# Register your custom model and admin class
admin.site.register(CustomUser, CustomUserAdmin)