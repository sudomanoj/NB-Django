from django import forms
from product_app.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Product name here'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }