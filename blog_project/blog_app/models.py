from django.db import models
from datetime import datetime
from taggit.models import Tag
from taggit.managers import TaggableManager
import django

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    author = models.CharField(max_length=30)
    published_date = models.DateField(editable=False, default=django.utils.timezone.now)
    
    class Meta:
        unique_together = ('title', 'content', 'author')
    def __str__(self):
        return self.title
    

class MetaData(models.Model):
    comment = models.CharField(max_length=100)
    tags = TaggableManager()
    post = models.ManyToManyField(Post, related_name='comment')