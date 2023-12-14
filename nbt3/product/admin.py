from django.contrib import admin
from product.models import Student, Course, Enrollment

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']

@admin.register(Course)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    
@admin.register(Enrollment)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'date']