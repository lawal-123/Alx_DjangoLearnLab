from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.db import connection, models
from .models import Book # Assuming a simple Book model
from .forms import BookSearchForm # Assuming you create this form
from .forms import ExampleForm
def book_search(request):
    search_results = Book.objects.none()
    form = BookSearchForm(request.GET)

    if form.is_valid():
        # Step 3: Secure Data Access (SQL Injection Prevention)
        # 1. Input is validated and sanitized by Django Forms.
        query = form.cleaned_data.get('query')

        if query:
            # 2. Use the Django ORM's 'filter' and 'icontains' methods.
            # The ORM handles all necessary query parameterization, making it safe.
            search_results = Book.objects.filter(
                models.Q(title__icontains=query) | models.Q(author__icontains=query)
            )
            
    context = {
        'form': form,
        'search_results': search_results,
        'query': query if 'query' in locals() else '',
    }
    
    # 3. Template Rendering: By default, Django templates automatically escape 
    # potentially harmful characters (like '<', '>', '&') when displaying variables 
    # (e.g., {{ query }}), which is the primary defense against non-context-aware XSS.
    return render(request, 'bookshelf/book_list.html', context)


# Example of a DANGEROUS function (DO NOT USE THIS APPROACH)
def dangerous_search_view(request):
    # DANGER: THIS IS VULNERABLE TO SQL INJECTION!
    # A malicious user could set 'search_term' to: 'title' OR 1=1 --
    search_term = request.GET.get('term', '') 
    
    # This direct string interpolation is a major security flaw.
    # NEVER DO THIS!
    # sql_query = f"SELECT * FROM bookshelf_book WHERE title = '{search_term}';" 

    # CORRECT WAY FOR RAW SQL (If ORM cannot be used):
    # Use the connection.cursor().execute() method with a tuple of parameters.
    # The database adapter handles the escaping/parameterization.
    if search_term:
        with connection.cursor() as cursor:
            # The query string uses '%s' as a placeholder.
            # The second argument is a tuple of values to be substituted.
            cursor.execute("SELECT * FROM bookshelf_book WHERE title = %s", [search_term]) 
            # Process results safely...

    return render(request, 'bookshelf/book_list.html', {})

from .models import Book
# Assuming you have a form for the Book model
# from .forms import BookForm 

# --- Permission-Protected Views ---

# 1. View Protected by can_view (Access Control)
@permission_required('library.can_view', raise_exception=True)
def book_list_view(request):
    """
    Allows users with the 'can_view' permission to see the list of books.
    Unauthorized users will receive a 403 Forbidden error (due to raise_exception=True).
    """
    books = Book.objects.all()
    context = {'books': books}
    
    # Placeholder: In a real app, this would render a template
    # return render(request, 'library/book_list.html', context)
    return HttpResponse(f"<h1>Book List</h1><p>You have the 'can_view' permission. Total books: {books.count()}</p>")


# 2. View Protected by can_create
@permission_required('library.can_create', raise_exception=True)
def book_create_view(request):
    """
    Only users with the 'can_create' permission can access this view.
    """
    if request.method == 'POST':
        # form = BookForm(request.POST)
        # if form.is_valid():
        #     new_book = form.save(commit=False)
        #     new_book.author = request.user
        #     new_book.save()
        #     return redirect('book_list')
        pass # Placeholder for actual creation logic

    # Placeholder: In a real app, this would render a form
    # return render(request, 'library/book_form.html', {'form': form})
    return HttpResponse("<h1>Create New Book</h1><p>You have the 'can_create' permission to add a new book.</p>")


# 3. View Protected by can_edit
@permission_required('library.can_edit', raise_exception=True)
def book_edit_view(request, pk):
    """
    Only users with the 'can_edit' permission can modify a book.
    """
    # book = get_object_or_404(Book, pk=pk)
    # form = BookForm(request.POST or None, instance=book)
    # if request.method == 'POST' and form.is_valid():
    #     form.save()
    #     return redirect('book_list')

    # Placeholder for actual editing logic
    # return render(request, 'library/book_form.html', {'form': form, 'book': book})
    return HttpResponse(f"<h1>Edit Book ID: {pk}</h1><p>You have the 'can_edit' permission to modify this book.</p>")


# 4. View Protected by can_delete (Can also use DeleteView with mixins)
@permission_required('library.can_delete', raise_exception=True)
def book_delete_view(request, pk):
    """
    Only users with the 'can_delete' permission can remove a book.
    """
    # book = get_object_or_404(Book, pk=pk)
    # if request.method == 'POST':
    #     book.delete()
    #     return redirect('book_list')
    
    # Placeholder for actual deletion logic
    # return render(request, 'library/book_confirm_delete.html', {'book': book})
    return HttpResponse(f"<h1>Delete Book ID: {pk}</h1><p>You have the 'can_delete' permission to remove this book.</p>")