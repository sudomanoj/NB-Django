from django.shortcuts import render
from product.models import Student, Course, Enrollment

# Create your views here.
def show_data(request):
    enrollment = Enrollment.objects.select_related('student').all()
    courses = Course.objects.prefetch_related('student').all()
    course_list = []
    for course in courses:
        print(f'Name of course: {course.title} Students: {[student.name for student in course.student.all()]}')
        course_name = course.title
        student_list = [student.name for student in course.student.all()]

    return render(request, 'product/home.html', {'enrollments':enrollment, 'courses':courses})