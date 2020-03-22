from django import forms
from django.forms import ModelForm
from .models import Post, Tag, Category
from django.contrib import admin
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

class PostFormModel(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['slug', 'created_at', 'updated_at']
   

STATUS_CHOICE=[
        ('Draft', 'Draft'),
        ('Published', 'Published')
    ]

class PostForm(forms.Form):
    # User = settings.AUTH_USER_MODEL
    # author = forms.CharField(required=True, widget=forms.TextInput(attrs={
    #     'class': 'form-group col-md-3'
    # }))

    author_twitter_account = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'form-group col-md-6'
    }))
    
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-group col-md-6'
    }))
    
    sub_title = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-group col-md-6'
    }))
    
    image = forms.FileField(max_length=None, required=False)
    
    img_description = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-group col-md-6'
    }))

    body = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-group col-md-6'
    }))
    
    category = forms.ModelChoiceField(required=True, queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form-group col-md-6'
    }))
    
    tag = forms.ModelChoiceField(queryset=Tag.objects.all(), required=True, widget=forms.Select(attrs={
        'class': 'form-group col-md-6'
    }))
     
    status = forms.CharField(required=True, widget=forms.Select(choices=STATUS_CHOICE, attrs={
        'class': 'form-group col-md-3'
    }))

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
