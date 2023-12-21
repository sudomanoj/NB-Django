from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse
from blog_app.forms import PostForm, LoginForm, SignupForm, Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'blog_app/base.html')

@login_required(login_url='login')
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/post_list.html', {'posts':posts})

@login_required
def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog_app/post_detail.html', {'post':post})

def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
          form = PostForm(request.POST, request.FILES)
          if form.is_valid():
              title = form.cleaned_data['title']
              content = form.cleaned_data['content']
              author = request.user
              post = Post(title=title, content=content, author=author)
              post.save()
              messages.success(request, 'Post Added Successfully!')
              return redirect(reverse('add_post'))
        else:
            return HttpResponse('You must be authenticated to add post!')
    return render(request, 'blog_app/add_post.html', {'form':form})

@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Updated Successfully!')
                return redirect(reverse('post_list'))
        else:
            form = PostForm(instance=post)

        return render(request, 'blog_app/update_post.html', {'form':form})
    else:
        return HttpResponse('<h1>You are not permitted to update</h1>')
    
    
@login_required    
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if (request.method == 'POST' and request.user == post.author):
        post.delete()
        messages.success(request, 'Post deleted Successfully!')
        return redirect(reverse('post_list'))
    else:
        return HttpResponse('<h1>You are not permitted to Delete</h1>')
    
    
def user_login(request):
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!')
                    return redirect(reverse('home'))
        
        return render(request, 'blog_app/login.html', {'form':form})
        
    else:
        return redirect(reverse('home'))

def user_signup(request):
    if not request.user.is_authenticated:
        form = SignupForm()
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('login'))

        return render(request, 'blog_app/signup.html', {'form':form})

