from django.urls import path
from blog_app import views
from auth_user import views as av

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('post_detail/<int:id>/', views.Post_Detail_View.as_view(), name='post_detail'),
    path('update_post/<int:id>/', views.update_post, name='update_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('signup/', views.user_signup, name='signup'),
    path('verify_otp/', views.verify_otp, name='verify_otp')
]
