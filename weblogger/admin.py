from django.contrib import admin

# Register your models here.
from .models import Post, Tag, Category

class PostAdmin(admin.ModelAdmin):
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