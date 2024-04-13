from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'genre', 'author', 'cost', 'buyer'
    )
    list_filter = (
        'name', 'genre', 'author', 'cost', 'buyer'
    )
    search_fields = (
        'name', 'genre', 'author', 'cost', 'buyer'
    )

# Register your models here.
