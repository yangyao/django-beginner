# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
import markdown2
from .models import Article, Category
# Create your views here.


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, ['fenced-code-blocks'])
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'
    # 接收url中的参数作为主键
    pk_url_kwarg = 'article_id'

    # 对数据做一个包装处理
    def get_object(self, queryset=None):
        obj = super(ArticleDetailView,self).get_object()
        obj.body = markdown2.markdown(obj.body, ['fenced-code-blocks'])
        return obj

    # 增加额外的数据
    def get_context_data(self, **kwargs):
        kwargs['category_lists'] = Category.objects.all().order_by('name')
        return super(ArticleDetailView, self).get_context_data(**kwargs)


class CategoryView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['category_id'], status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, ['fenced-code-blocks'])
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(CategoryView, self).get_context_data(**kwargs)
