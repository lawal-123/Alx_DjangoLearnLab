from django.contrib import admin
from .models import Book
admin.site.register(Book)


list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
