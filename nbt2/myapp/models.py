from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    
    class Meta:
        verbose_name = 'Author Name'
        ordering = ['-name']
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey("Author", verbose_name="author", on_delete=models.CASCADE)
    published_date = models.DateField()
    
    class Meta:
        verbose_name = 'Pustak'

