# Generated by Django 4.1.3 on 2023-01-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_commentmodel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='time',
            field=models.CharField(default='Fri Jan 13 00:14:08 2023', max_length=100),
        ),
    ]