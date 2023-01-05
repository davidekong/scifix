from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=1000)


class CommentModel(models.Model):
    comment_text = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    time = models.CharField(max_length=100, default=datetime.datetime.today().ctime())

class CustomUser(models.Model):
    email = models.EmailField(unique=True, default=None)
    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)
    pic = models.ImageField(upload_to='blog/media')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Subscribers(models.Model):
    email = models.EmailField(unique=True, default=None)
    reason = models.TextField(max_length=1000, default=None)