from django.urls import path, include
from . import views

urlpatterns = [
    #Blog Post URLs
    path('', views.homepage, name='Home'),
    path('about/', views.get_about, name='About'),
    path('blog/', views.all_posts, name='All Posts'),
    path('blog/<slug:slug>/', views.read_post, name='post_detail'),
    path('blog/create/', views.post_form, name='New Post')
]