<<<<<<< HEAD
from django.contrib import admin
from .models import Book
admin.site.register(Book)
=======
from django.contrib import admin
from .models import Book
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ("publication_year", "author")
admin.site.register(Book, BookAdmin)
>>>>>>> 833a1e0c4ff758225723255cb9e94e655d996c89
