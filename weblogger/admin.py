from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post, Tag, Category


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['slug', 'created_at', 'updated_at']


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'sub_title', 'author', 'author_twitter_account', 'slug')
    prepopulated_fields = {'title' : ('sub_title', 'author_twitter_account',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'slug')
    # prepopulated_fields = {'id' : ('tag_name', 'slug')}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'slug')
    # prepopulated_fields = {'id' : ('cat_name', 'slug')}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)    
# admin.site.register(Post, PostAdmin) 