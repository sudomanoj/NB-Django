from django.shortcuts import render
from blog_app.models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def show_posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/post_list.html', {'posts':posts})

def show_posts_detail(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/post_detail.html', {'posts':posts})

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')

        """ Create the Post """
        try:
            post = Post(title=title, content=content, author=author)
            post.save()
            return HttpResponseRedirect(reverse('post_detail'))
        except:
            return HttpResponseRedirect(reverse('create_post'))
    return render(request, 'blog_app/create_post.html')
