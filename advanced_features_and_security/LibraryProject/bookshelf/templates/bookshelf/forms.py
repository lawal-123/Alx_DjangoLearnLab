# LibraryProject/bookshelf/forms.py

from django import forms

class BookSearchForm(forms.Form):
    """
    Form to handle the book search input. 
    Using a Django Form ensures the input is cleaned, validated, and 
    sanitized, which is a critical part of preventing security issues 
    like Cross-Site Scripting (XSS) and ensuring data integrity.
    """
    # Define a character field for the search query
    query = forms.CharField(
        label='Search for books or authors', 
        max_length=100,
        required=False, # The search query is optional
        # Using a Widget to add attributes like a placeholder
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter title or author'
        })
    )
    # Example of ExampleForm (if required)
class ExampleForm(forms.Form):
    # Add relevant fields here
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')