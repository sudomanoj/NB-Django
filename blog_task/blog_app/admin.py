from django.contrib import admin
from blog_app.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'create_date', 'update_date', 'author']