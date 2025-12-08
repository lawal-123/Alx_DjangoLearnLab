# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
TagWidget()
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
# blog/forms.py (Add this to your existing file)
from django import forms
from .models import Comment
# ... (Your existing forms like PostForm, BlogUserCreationForm)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Only the content is input by the user. post and author are set by the view.
        fields = ['content'] 
        
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your comment here...'}),
        }
# blog/forms.py (Update PostForm)
from django import forms
from .models import Post, Comment
# ... (other imports)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Include 'tags' in the fields list
        fields = ['title', 'content', 'tags'] 
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            # django-taggit automatically uses a suitable widget, but we can style it:
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tags separated by commas, e.g., django, python, tutorial'}),
        }
# ... (rest of the forms remain unchanged)
