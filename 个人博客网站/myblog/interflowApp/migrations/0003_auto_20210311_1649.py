# Generated by Django 3.1.5 on 2021-03-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interflowApp', '0002_board_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='user',
        ),
        migrations.AlterField(
            model_name='board',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
