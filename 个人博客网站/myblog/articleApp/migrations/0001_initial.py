# Generated by Django 3.1.5 on 2021-03-09 08:21

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='博文标题')),
                ('description', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('tag', models.CharField(choices=[('python基础', 'python基础'), ('python-GUI', 'python-GUI'), ('django-web', 'django-web'), ('Java基础', 'Java基础'), ('Java-GUI', 'Java-GUI'), ('其他', '其他')], max_length=50, verbose_name='博客类型')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
            ],
            options={
                'verbose_name': '博文',
                'verbose_name_plural': '博文',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, verbose_name='评论内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articleApp.blog_post', verbose_name='所属文章')),
            ],
            options={
                'verbose_name': '评论管理',
                'verbose_name_plural': '评论管理',
            },
        ),
    ]
