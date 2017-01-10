# encoding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now_add=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True, help_text='可选，如果为空，截取正文的54个字符')
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category',verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


class Category(models.Model):
    name = models.CharField('名称', max_length=30)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('名称', max_length=30)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now_add=True)


class Blog(models.Model):
    title = models.CharField('标题', max_length=10)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)
    category = models.ForeignKey('Category', verbose_name='分类')
    tags = models.ManyToManyField('Tag', verbose_name='标签')

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='博客')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.TextField('内容')
    created = models.DateTimeField('发布时间', auto_now_add=True)




