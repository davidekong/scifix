# Generated by Django 4.1.3 on 2023-01-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_subscribers_alter_commentmodel_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='reason',
            field=models.TextField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='time',
            field=models.CharField(default='Tue Jan  3 16:09:19 2023', max_length=100),
        ),
    ]