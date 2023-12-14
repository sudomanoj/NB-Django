from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(null=False)
    
    def __str__(self):
        return self.name
    

class Course(models.Model):
    title = models.CharField(max_length=100)
    student = models.ManyToManyField(Student, through='Enrollment')
    
    def __str__(self):
        return self.title
    

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = datetime.date.today()