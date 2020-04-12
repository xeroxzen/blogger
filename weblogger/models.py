from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings

# Create your models here.
class Post(models.Model):
    STATUS_CHOICE = (
        ('PUBLISHED', 'Published'),
        ('DRAFT', 'Draft')
    )

    User = settings.AUTH_USER_MODEL
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    author_twitter_account = models.CharField(max_length=80)
    # author_email_address = models.EmailField(max_length=254)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, height_field=None, width_field=None, max_length=None, blank=False)
    img_description = models.CharField(max_length=255, null=False, default='')
    content = RichTextUploadingField()
    category = models.ForeignKey("Category", verbose_name=("Category"), related_name='category', on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField("Tag", verbose_name=("Tag"), related_name='tag')
    slug = models.SlugField(max_length=60, unique=True, editable=False, default=None)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        name = self.title
        self.slug = slugify(name, allow_unicode=True)
        super().save(*args, **kwargs)        

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        ordering = ['-id', 'created_at', 'updated_at', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})

    def snippet(self):
        return self.content[0:200]    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    website = models.URLField(max_length=200, null=True, blank=True)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)

class Category(models.Model):
    cat_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=60, unique=True, editable=False, default=None)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        name = self.cat_name
        self.slug = slugify(name, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

class Tag(models.Model):
    tag_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=60, unique=True, editable=False, default=None)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        name = self.tag_name
        self.slug = slugify(name, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Messages'