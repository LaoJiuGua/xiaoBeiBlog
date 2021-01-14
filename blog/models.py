from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
# Create your models here.


class Category(models.Model):
    """ 分类 """

    name = models.CharField('分类名', max_length=100)


class Tag(models.Model):
    """ 标签 """

    name = models.CharField('标签名', max_length=100)


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #标签
    tags = models.ManyToManyField(Tag, blank=True)
    # 创建时间
    created_time = models.DateTimeField('创建时间', default=datetime.now)
    # 修改时间
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Mate:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ('-created_time',)

    def __str__(self):
        return self.title
