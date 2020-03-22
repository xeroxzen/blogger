from django.urls import path, include
from . import views

urlpatterns = [
    #Blog Post URLs
    path('', views.homepage, name='Home'),
    path('blog/', views.all_posts, name='All Posts'),
    path('blog/<int:id>/', views.read_post, name='Post'),
    path('blog/create/', views.post_form, name='New Post')
]