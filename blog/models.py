import re

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
import markdown
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.html import strip_tags
# Create your models here.
from markdown.extensions.toc import TocExtension, slugify
from markdown.treeprocessors import Treeprocessor

class Category(models.Model):
    """ 分类 """

    name = models.CharField('分类名', max_length=100)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """ 标签 """

    name = models.CharField('标签名', max_length=100)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


def generate_rich_content(value):
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.attr_list",
            "markdown.extensions.codehilite",
            'markdown.extensions.fenced_code',
            'markdown.extensions.tables',
            'markdown.extensions.sane_lists',
            # 记得在顶部引入 TocExtension 和 slugify
            TocExtension(slugify=slugify),
        ]
    )
    content = md.convert(value)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    toc = m.group(1) if m is not None else ""
    return {"content": content, "toc": toc}

class Post(models.Model):
    """
        文章表
    """

    title = models.CharField('文章标题', max_length=70)
    # 文章正文
    body = models.TextField('文章正文')
    # 文章载要
    excerpt = models.CharField('文章载要', max_length=200, blank=True)
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章作者')
    # 分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    #标签
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    # 创建时间
    created_time = models.DateTimeField('创建时间', default=datetime.now)
    # 修改时间
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    # 阅读量
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ('-created_time',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            'markdown.extensions.codehilite',
            'markdown.extensions.sane_lists',

        ])
        # 先将 Markdown 文本渲染成 HTML 文本
        # strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 从文本摘取前 54 个字符赋给 excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:54]

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    @property
    def toc(self):
        return self.rich_content.get("toc", "")

    @property
    def body_html(self):
        return self.rich_content.get("content", "")

    @cached_property
    def rich_content(self):
        return generate_rich_content(self.body)


