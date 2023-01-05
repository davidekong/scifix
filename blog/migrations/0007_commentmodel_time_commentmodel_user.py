# Generated by Django 4.1.3 on 2022-12-31 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_customuser_email_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='time',
            field=models.CharField(default='Sat Dec 31 02:43:17 2022', max_length=100),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
