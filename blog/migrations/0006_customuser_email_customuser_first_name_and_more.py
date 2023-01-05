# Generated by Django 4.1.3 on 2022-12-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_customuser_delete_customusermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
