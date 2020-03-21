from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'author', 'author_twitter_account', 'slug')
    prepopulated_fields = {'title' : ('sub_title', 'author_twitter_account',)}

admin.site.register(Post, PostAdmin)    