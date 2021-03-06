# Generated by Django 3.0.4 on 2020-04-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblogger', '0023_auto_20200408_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=10, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Mail List',
            },
        ),
    ]
