from django.contrib import admin

# Register your models here.

from blog.models import Category, Tag, Blog, Comment

admin.site.register([Category, Tag, Blog, Comment])
