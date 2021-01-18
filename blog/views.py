import re
import markdown
# from django.core.checks import messages
from django.contrib import messages
from django.db.models import Q
from markdown.extensions.toc import TocExtension

from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from pure_pagination import PaginationMixin

from .models import Category, Tag, Post

# Create your views here.

# def article_list(request):
#     """ 文章列表 """
#     articles = Post.objects.all()
#
#
#     return render(request, 'index.html', {
#         "articles": articles,
#
#     })


# def article_detail(request, pk):
#     """ 详情 """
#     post = get_object_or_404(Post, pk=pk)
#     # 阅读量+1
#     post.increase_views()
#
#     md = markdown.Markdown(extensions=[
#                                       'markdown.extensions.extra',
#                                       'markdown.extensions.codehilite',
#                                       # 'markdown.extensions.toc',
#                                       TocExtension(slugify=slugify),
#                                   ])
#
#     post.body = md.convert(post.body)
#     m =re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
#     post.toc = m.group(1) if m is not None else ''
#
#     return render(request, 'single.html', {
#         "post": post,
#     })


# def archive(request, year, month):
#     articles = Post.objects.filter(created_time__year=year,
#                                     created_time__month=month
#                                     ).order_by('-created_time')
#     return render(request, 'index.html', {'articles': articles})


# def category(request, pk):
#     # 记得在开始部分导入 Category 类
#     cate = get_object_or_404(Category, pk=pk)
#     articles = Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request, 'index.html', {'articles': articles})


# def tag(request, pk):
#     # 记得在开始部分导入 Tag 类
#     t = get_object_or_404(Tag, pk=pk)
#     articles = Post.objects.filter(tags=t).order_by('-created_time')
#     return render(request, 'index.html', {'articles': articles})


def search(request):
    q = request.GET.get('q')

    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('index')

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'index.html', {'articles': post_list})


def guidance(request):
    return render(request, 'guidance.html', )


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


class IndexView(PaginationMixin,ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'single.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    # def get_object(self, queryset=None):
    #     post = super().get_object(queryset=None)
    #     md = markdown.Markdown(extensions=[
    #         'markdown.extensions.extra',
    #         'markdown.extensions.codehilite',
    #         # 'markdown.extensions.toc',
    #         TocExtension(slugify=slugify),
    #     ])
    #     post.body = md.convert(post.body)
    #     m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    #     post.toc = m.group(1) if m is not None else ''
    #
    #     return post


class ArchiveView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Post.objects.filter(created_time__year=self.kwargs.get('year'),
                                       created_time__month=self.kwargs.get('month')).order_by('-created_time')
        # return super(ArchiveView, self).get_queryset().filter(articles=articles)
        return articles


class CategoryView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class TagView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        t = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=t)


# 404
def page_not_found(request, exception):  # 注意点 ①
    return render(request, '404.html')

# # 500
# def page_error(request):
#     return render(request, '500.html')