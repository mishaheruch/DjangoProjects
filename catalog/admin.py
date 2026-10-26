from django.contrib import admin

from .models import Book, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin): #регестрація в адмінці моделів і фільтр, пошук
    search_fields = ('title', 'author')
    list_filter = ('stock', 'author')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
