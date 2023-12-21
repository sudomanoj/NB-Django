from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
    path('update_post/<int:id>/', views.update_post, name='update_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('signup/', views.user_signup, name='signup'),
]
