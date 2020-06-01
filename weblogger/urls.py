from django.urls import path, include
from . import views
from .views import CategoryListView

urlpatterns = [
    #Blog Post URLs
    path('', views.homepage, name='Home'),
    path('about/', views.get_about, name='About'),
    path('blog/', views.all_posts, name='All Posts'),
    path('tweet_list/', views.tweet_list, name='Tweet List'),
    path('tweet_fetch/', views.tweet_fetch, name='Tweet Fetch'),
    path('tweet_active/', views.tweet_set_active, name='Tweet Set Active'),
    path('tweet_inactive/', views.tweet_set_inactive, name='Tweet Set Inactive'),
    path('create/', views.post_form, name='New Post'),
    path('blog/<slug:slug>/', views.read_post, name='post_detail'),
    path('category/<int:pk>', CategoryListView.as_view(), name='post-category'),
    path('contact/', views.contact, name='Contact'),
    # path('tags/<slug:slug>/', views.get_post_by_tag, name='tag_detail'),
    # path('Category_detail')
    # path('blog/<tag:tag>/', views.get_post_by_tag, name='post by tag'),
]
