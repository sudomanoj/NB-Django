from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from product_app.models import Product
from product_app.forms import ProductForm
from django.contrib import messages
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
            messages.success(request, 'Product Added Successfully')
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

def update_product(request, id):
    try:
        product = Product.objects.get(id=id)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product Updated successfully!')
                return redirect('/')
        else:
            form = ProductForm(instance=product)
        return render(request, 'product_app/update_product.html', {'form':form})
    except:
        return HttpResponse('Product is not in the database!')
    
def delete_product(request, id):
    try:
        product = Product.objects.get(id=id)
        print(product)
        if request.method == 'POST':
            product.delete()
            messages.success(request, 'Product deleted Successfully!')
            return redirect('/')
        # return render(request, 'product_app/product_detail.html')
    except Exception as e:
        return HttpResponse(e)
    