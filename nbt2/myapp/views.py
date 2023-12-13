from django.shortcuts import render
from myapp.models import Author, Book
# Create your views here.

def home(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'myapp/home.html', {'books':books})
        
