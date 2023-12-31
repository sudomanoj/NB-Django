from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_list/', views.show_posts_list, name='post_list'),
    path('post_detail/<int:id>/', views.show_posts_detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
]
