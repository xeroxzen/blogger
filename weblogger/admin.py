from django.contrib import admin
# from django import forms
# from ckeditor.widgets import CKEditorWidget
from .models import Post, Comment, Tag, Category, NewsLetter, Tweet, Contact


class PostAdmin(admin.ModelAdmin):
    # form = PostAdminForm
    list_display = ('title', 'sub_title', 'author', 'slug', 'status')
    prepopulated_fields = {'title' : ('sub_title', 'author_twitter_account',)}
    search_fields = ('title', 'sub_title', 'content')
    actions = ['status']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)    

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'slug')
    # prepopulated_fields = {'id' : ('tag_name', 'slug')}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'slug')
    # prepopulated_fields = {'id' : ('cat_name', 'slug')}

class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('username', 'your_email', 'active', 'created_at')
    search_fields = ('username', 'your_email')
    actions = ['approve_newsletter']

    def approve_newsletter(self, request, queryset):
        queryset.update(active=True)    

class TweetAdmin(admin.ModelAdmin):
    list_display=('tweet_id', 'tweet_text', 'published_date', 's_active')
    search_fields=('tweet_id', 'tweet_text')
    actions=['approve_tweet']

    def approve_tweet(self, request, query_set):
        query_set.update(is_active=True)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    prepopulated_fields = {'name' : ('email', 'message')}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)    
admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(Tweet, TweetAdmin) 