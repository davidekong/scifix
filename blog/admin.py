from django.contrib import admin
from blog.models import Post, CommentModel, CustomUser, Subscribers
from django.contrib.sites.models import Site
# Register your models here.
admin.site.register(Post)
admin.site.register(CommentModel)
admin.site.register(CustomUser)
admin.site.register(Subscribers)
