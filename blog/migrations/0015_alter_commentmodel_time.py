# Generated by Django 4.1.3 on 2023-01-12 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_commentmodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='time',
            field=models.CharField(default='Thu Jan 12 23:57:57 2023', max_length=100),
        ),
    ]