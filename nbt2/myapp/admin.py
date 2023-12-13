from django.contrib import admin
from myapp.models import Author, Book

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'bio']
    
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'display_author', 'published_date']
    def display_author(self, obj):
        return obj.author.name

    display_author.short_description = 'Author'