from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse
from blog_app.forms import PostForm, LoginForm, SignupForm, Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from auth_user.views import *
from auth_user .managers import CustomUserManager
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog_app/base.html')

# @login_required(login_url='user_login')
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog_app/post_list.html', {'posts':posts})

class PostListView(LoginRequiredMixin, View):
    login_url = 'user_login'

    def get(self, request):
        posts = Post.ogjects.all()
        return render(request, 'blog_app/post_list.html', {'posts':posts})

    
    
# @login_required
# def post_detail(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'blog_app/post_detail.html', {'post':post})

class Post_Detail_View(LoginRequiredMixin, View):
    login_url = 'user_login'
    def get(self, request, id, *args, **kwargs):
        post = get_object_or_404(Post, id=id)
        return render(request, 'blog_app', {'post':post})

# def add_post(request):
#     form = PostForm()
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#           form = PostForm(request.POST, request.FILES)
#           if form.is_valid():
#               title = form.cleaned_data['title']
#               content = form.cleaned_data['content']
#               author = request.user
#               post = Post(title=title, content=content, author=author)
#               post.save()
#               messages.success(request, 'Post Added Successfully!')
#               return redirect(reverse('add_post'))
#         else:
#             return HttpResponse('You must be authenticated to add post!')
#     return render(request, 'blog_app/add_post.html', {'form':form})

class AddPostView(LoginRequiredMixin, View):
    login_url = 'user_login' 
    def get(self, request):
        return render(request, 'blog_app/add_post.html', {'form': form})
    
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = request.user
            post = Post(title=title, content=content, author=author)
            post.save()
            messages.success(request, 'Post Added Successfully!')
            return redirect(reverse('add_post'))
        return render(request, 'blog_app/add_post.html', {'form': form})


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
    
    
from django.contrib import messages

def user_login(request):
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!')
                    return redirect(reverse('home'))
                else:
                    messages.error(request, 'Invalid username or password.')
            else:
                messages.error(request, 'Form is not valid.')

        return render(request, 'blog_app/login.html', {'form': form})
    else:
        return redirect(reverse('home'))


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Save the user without committing to the database
            user_manager = CustomUserManager()
            user = user_manager.create_user(
                email = form.cleaned_data['email'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
            )
            # Generate OTP and associate with the user
            totp_device, created = TOTPDevice.objects.get_or_create(user=user)
            otp_code = totp_device.generate_otp()
            OTP.objects.create(user=user, totp_device=totp_device, otp_code=otp_code)
            # Send the OTP code to the user via email
            send_otp_via_email(otp_code, user.email)
            # Redirect to the OTP verification page
            return redirect('verify_otp')  # Replace 'verify_otp' with your actual URL
    else:
        form = SignupForm()

    return render(request, 'blog_app/signup.html', {'form': form})



def send_otp_via_email(otp, email):
    subject = 'Your one-time Password (OTP)'
    message = f'Your OTP is {otp}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)



@login_required
def verify_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp_code']

            # Retrieve the OTP record from the database
            otp_record = OTP.objects.filter(user=request.user, otp_code=otp_code).first()

            if otp_record and otp_record.totp_device.verify_otp(otp_code):
                # OTP verification successful
                otp_record.delete()  # Remove the used OTP record
                login(request, request.user)  # Log in the user if needed
                return HttpResponse('OTP Verified Successfully!')
            else:
                # Invalid OTP
                form.add_error('otp_code', 'Invalid OTP. Please try again.')
    else:
        form = OTPForm()

    return render(request, 'blog_app/verify_otp.html', {'form': form})



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return HttpResponse('You must be loggedin first')
