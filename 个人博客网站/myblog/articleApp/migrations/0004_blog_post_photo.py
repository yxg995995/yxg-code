# Generated by Django 3.1.5 on 2021-03-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleApp', '0003_remove_blog_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Article/'),
        ),
    ]
