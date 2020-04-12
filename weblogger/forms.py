from django import forms
from django.forms import ModelForm
from .models import Post, Comment, Tag, Category, Contact
from django.contrib import admin
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ('author', 'author_twitter_account', 'title', 'sub_title', 'image', 'img_description', 'content', 'tag', 'category', 'status')
        # exclude = ['slug', 'created_at', 'updated_at']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'website','comment')   

STATUS_CHOICE=[
        ('Draft', 'Draft'),
        ('Published', 'Published')
    ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']