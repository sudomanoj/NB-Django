from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    create_date = models.DateField(auto_now_add=True, editable=False)
    update_date = models.DateField(auto_now=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('title', 'content')