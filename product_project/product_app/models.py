from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='product_image')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    created = models.DateField(editable=False, auto_now_add=True)
    updated = models.DateField(editable=False, auto_now=True)
    

    
    def __str__(self):
        return self.name
    
class Shopkeeper(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    