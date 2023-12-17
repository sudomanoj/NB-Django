from django.contrib import admin
from product_app.models import Product
from django.utils.html import format_html
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'name', 'display_image', 'price', 'description', 'created', 'updated']
    
    
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)

    display_image.short_description = 'Image'
    display_image.allow_tags = True