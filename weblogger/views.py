from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Category, Tag
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PostForm, CommentForm, NewsletterForm, ContactForm
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
    template = 'weblogger/read_post.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    mail_list = None

    # Newsletter Sign Ups
    # newsletter_form = NewsletterForm()
    if request.method == 'POST':
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            # create newsletter objects
            mail_list = newsletter_form.save(commit=False)
            mail_list.save()

            # messages
            messages.success(
                request, 'Newsletter subscription successful', extra_tags='alert')
            return HttpResponseRedirect('')    

        else:
            messages.warning(
                request, 'Please correct the error and then proceed', extra_tags='alert')
    else:
        newsletter_form = NewsletterForm()
        
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
        'title':post.title,
        'comments':comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'newsletter_form': newsletter_form,
        'mail_list': mail_list,
        'action': 'Subscribe',
    }
    return render(request, template, context)

# @login_required
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
        'form':form,
        'button':'Post'
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


@login_required
def tweet_list(request):
    tweets = Tweet.objects.order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(tweets, 10)
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)
    return render(request, 'weblogger/tweets.html', {'tweets': tweets})


@login_required
def tweet_set_inactive(request, pk):
    set_inactive(pk)
    return redirect('tweets')


@login_required
def tweet_set_active(request, pk):
    set_active(pk)
    return redirect('tweets')


@login_required
def tweet_fetch(request):
    save_to_db()
    return redirect('tweets')

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

    return render(request, 'weblogger/contact.html', context)
