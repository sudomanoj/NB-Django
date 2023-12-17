from django.shortcuts import render, redirect
from django.http import HttpResponse
from product_app.models import Product
from product_app.forms import ProductForm
# Create your views here.

def home(request):
    return render(request, 'product_app/base.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name=form.cleaned_data["name"]
            image=form.cleaned_data["image"]
            price=form.cleaned_data["price"]
            description=form.cleaned_data["description"]
            product=Product(name=name,price=price,description=description,image=image)
            product.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'product_app/add_product.html', {'form':form})

def show_product_list(request):
    products = Product.objects.all()
    return render(request, 'product_app/product_list.html', {'products':products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_app/product_detail.html', {'product':product})