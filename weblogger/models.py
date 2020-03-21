from django.db import models
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
class Post(models.Model):
    STATUS_CHOICE =(
        ('PUBLISHED', 'Published'),
        ('DRAFT', 'Draft')
    )

    User = settings.AUTH_USER_MODEL
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    author_twitter_account = models.CharField(max_length=80)
    author_email_address = models.EmailField(max_length=254)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    post_img = models.ImageField(upload_to='images/', null=True, height_field=None, width_field=None, max_length=None)
    body = models.TextField()
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})