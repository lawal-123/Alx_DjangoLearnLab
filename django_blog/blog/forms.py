# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogUserCreationForm(UserCreationForm):
    # Add email field and make it required
    email = forms.EmailField(required=True) 

    class Meta:
        # Use the default User model
        model = User
        # Include all default fields plus the new email field
        fields = ("username", "email", "first_name", "last_name") 

    def save(self, commit=True):
        # Call the parent save method to create the user
        user = super().save(commit=False)
        # Set the email field from the form data
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
# blog/forms.py (Add this to your existing file)
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Fields the user will input via the form
        fields = ['title', 'content'] 
        # Optional: Add form widgets for better appearance/control
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }