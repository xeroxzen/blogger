# Generated by Django 3.0.4 on 2020-03-21 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_twitter_account', models.CharField(max_length=80)),
                ('author_email_address', models.EmailField(max_length=254, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('post_img', models.ImageField(null=True, upload_to='images/')),
                ('body', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('PUBLISHED', 'Published'), ('DRAFT', 'Draft')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
