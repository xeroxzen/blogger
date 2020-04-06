from django.contrib import admin
# from django import forms
# from ckeditor.widgets import CKEditorWidget
from .models import Post, Comment, Tag, Category


class PostAdmin(admin.ModelAdmin):
    # form = PostAdminForm
    list_display = ('title', 'sub_title', 'author', 'slug', 'status')
    prepopulated_fields = {'title' : ('sub_title', 'author_twitter_account',)}
    search_fields = ('title', 'sub_title', 'content')

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

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)    
# admin.site.register(Post, PostAdmin) 