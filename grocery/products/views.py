from django.shortcuts import render

def home(request):
    context = {'name':'Network Adapter', 'price':1500}
    return render(request, 'home.html', context)
