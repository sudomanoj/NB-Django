from django.contrib import admin
from blog_app.models import Post, MetaData

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'author', 'published_date']

@admin.register(MetaData)
class MetaDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment',]