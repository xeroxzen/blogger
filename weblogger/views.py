from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Category, Tag
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PostForm, CommentForm, ContactForm
from django.views.generic import ListView

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
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
    posts = Post.objects.filter(status='PUBLISHED')
    paginator = Paginator(posts, 20)
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

def tag(request, slug):
    tags = get_object_or_404(Tag, slug=slug)

    context={
        'tags': tags
    }

    return render(request, 'weblogger/tags.html', context)

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

@login_required
def post_form(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Create post object but don't save yet.
            new_post = form.save(commit=False)

            new_post.user = request.user
            new_post.save()
            # post.save()

            messages.success(request, 'Post successfully added', extra_tags='alert')

            return HttpResponseRedirect('/')
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

class CategoryListView(ListView):
    model = Post
    template_name = 'blog/blog_category.html'

    def get_queryset(self):
        category = get_object_or_404(Category, id=self.kwargs.get('category__name'))
        return Post.objects.filter(category_id=self.kwargs.get('pk'))
    

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Messages sent successfully', extra_tags='alert')
            return HttpResponseRedirect('/blog')
        else:
            messages.warning(request, 'Message not sent, try again', extra_tags='alert')    
    else:
        form = ContactForm

    context={
        'form':form,
        'button': 'Send Message',
        'title': 'Get In Touch'
    }

    return render(request, 'weblogger/form.html', context)            

