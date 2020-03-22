from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm

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

    context={
        'post':post,
    }
    return render(request, 'weblogger/read_post.html', context)

# @login_required
def post_form(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(
                title = form.cleaned_data.get('title'),
                sub_title = form.cleaned_data.get('sub_title'),
                author_twitter_account = form.cleaned_data.get('author_twitter_account'),
                image = form.cleaned_data.get('image'),
                img_description = form.cleaned_data.get('img_description'),
                body = form.cleaned_data.get('body'),
                category = form.cleaned_data.get('category'),
                tag = form.cleaned_data.get('tag'),
                status = form.cleaned_data.get('status')
            )

            post.user = request.user
            post.save()

            messages.success(request, 'Post successfully added', extra_tags='alert')

            return HttpResponseRedirect('weblogger/index.html')
        else:
            messages.warning(request, 'Please correct the encountered errors', extra_tags='alerts')
    else:
        form = PostForm()

    context={
        'form':form
    }

    return render(request, 'weblogger/form.html', context)            


