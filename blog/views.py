from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
import markdown2
from .models import Blog, Comment, Article, Category
from .forms import CommentForm
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
        kwargs['category_lists'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)


def get_blog_lists(request):
    ctx = {
        'blog_lists': Blog.objects.all().order_by('-created')
    }
    return render(request, 'blog-list.html', ctx)


def get_blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog-detail.html', ctx)


def blog_add_comment(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/detail/'+str(blog_id)), {'form': form})

