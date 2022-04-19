from django.contrib import admin
from .models import Book, Author, BookCopies

class BookCopiesAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'status', 'due_back')
    list_filter = ['due_back']

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookCopies, BookCopiesAdmin)


