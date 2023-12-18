from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product_app import views

urlpatterns = [
    path('', views.home),
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.show_product_list, name='product_list'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
