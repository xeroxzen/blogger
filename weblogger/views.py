from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context={
        'title':'Homepage',
        'message':'Hello World',
        'posts': posts,
        'blog_name':"Andile's View Points"
    }
    return render(request, 'weblogger/index.html', context)

def all_posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    if request.method == 'GET':
        try:
            page = request.GET.get('page')
        except Exception:
            return HttpResponseRedirect('/')
    posts = paginator.get_page(page)

    context ={
        'title' : 'All Posts',
        'posts': posts
    }             

    return render(request, 'weblogger/blog.html', context)

def read_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'weblogger/read_post.html', context)       

