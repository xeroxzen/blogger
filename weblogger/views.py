from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm

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

def read_post(request, slug):
    template = 'read_post.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    # Comment Posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to db yet.
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post

            # Save the comment to db
            new_comment.save()
    else:
        comment_form = CommentForm()           

    context={
        'post':post,
        'comments':comments,
        'new_comment': new_comment,
        'comment_form': comment_form
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


def get_about(request):
    template = 'weblogger/about.html'

    context={
        'title':'About'
    }                

    return render(request, template, context)

def get_post_by_tag(request, tag):

    posts = Post.objects.get(tag='Elon Musk')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context={
        'posts':posts
    }
    return render(request, 'weblogger/blog.html', context)    


