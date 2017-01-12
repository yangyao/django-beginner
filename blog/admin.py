from django.contrib import admin

# Register your models here.

from blog.models import Category, Tag, Comment, Article

admin.site.register([Category, Tag, Comment, Article])
