import re

import markdown
from django.shortcuts import render, get_object_or_404
from .models import Category, Tag, Post

from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
# Create your views here.


def article_list(request):
    """ 文章列表 """
    articles = Post.objects.all()


    return render(request, 'index.html', {
        "articles": articles,

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
    post = get_object_or_404(Post, pk=pk)


    md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      # 'markdown.extensions.toc',
                                      TocExtension(slugify=slugify),
                                  ])

    post.body = md.convert(post.body)
    m =re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'single.html', {
        "post": post,
    })


def archive(request, year, month):
    articles = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'index.html', {'articles': articles})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    articles = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'index.html', {'articles': articles})


def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    articles = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'index.html', {'articles': articles})


# 404
def page_not_found(request,exception):  # 注意点 ①
    return render(request, '404/../templates/404.html')

# # 500
# def page_error(request):
#     return render(request, '500.html')