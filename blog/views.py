from django.shortcuts import render
from .models import Category, Tag, Post
# Create your views here.


def article_list(request):
    """ 文章列表 """
    articles = Post.objects.all()

    return render(request, 'index.html', {
        "articles": articles
    })


def full_width(request):
    """ 博客 """
    articles = Post.objects.all()

    return render(request, 'full-width.html', {
        "articles": articles
    })


def about(request):
    """ 联系 """
    return render(request, 'about.html')


def contact(request):
    """ 关于 """
    return render(request, 'contact.html')


def article_detail(request, pk):
    """ 详情 """
    article = Post.objects.get(pk=pk)

    return render(request, 'single.html', {
        "article": article
    })