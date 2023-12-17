from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product_app import views

urlpatterns = [
    path('', views.home),
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.show_product_list, name='product_list'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
