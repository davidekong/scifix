# Generated by Django 4.1.3 on 2023-05-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_commentmodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='time',
            field=models.CharField(default='Sat May  6 16:02:29 2023', max_length=100),
        ),
    ]
