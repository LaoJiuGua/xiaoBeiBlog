# 小北博客

### 开发环境

- Windows 10
- Python3.7.9
- Django最新版

### 目录结构

```pytyon
blog\
	- __init__.py
	- admin.py
	- apps.py
	migrations\
		__init__.py
	- models.py
	- tests.py
	- views.py
xiaoBeiBlog\
	- __init__.py
	- asgi.py
	- settings.py
	- urls.py
	- wsgi.py
- manage.py
```

### 数据库模型

- 数据库表结构

  - 文章(```Post```)表

    | 文章ID | 标题  | 正文 | 作者 | 分类   | 标签   | 发表时间  |
    | ------ | ----- | ---- | ---- | ------ | ------ | --------- |
    | 1      | Title | Text | 鲁迅 | Django | Python | 2021-1-14 |

  - 分类(```Category```)表

    | 分类ID | 分类名 |
    | ------ | ------ |
    | 1      | Django |

  - 标签(```Tag```)表

    | 标签ID | 标签名 |
    | :----- | ------ |
    | 1      | Python |

  - 代码

    ```python
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
    ```

    ### Markdown 语法和代码高亮

    让博客文章具有良好的排版，显示更加丰富的格式，使用 Markdown 语法来书写博文。Markdown 是一种 HTML 文本标记语言，只要遵循它约定的语法格式，Markdown 的解析工具就能够把 Markdown 文档转换为标准的 HTML 文档，从而使文章呈现更加丰富的格式，例如标题、列表、代码块等等 HTML 元素。由于 Markdown 语法简单直观，不用超过 5 分钟就可以轻松掌握常用的标记语法，因此大家青睐使用 Markdown 书写 HTML 文档。下面让我们的博客也支持使用 Markdown 写作。

    - #### 安装 Python Markdown

      ```python
      pip install markdown
      ```

    - #### 在 detail 视图中解析 Markdown

      将 Markdown 格式的文本解析成 HTML 文本非常简单，只需调用这个库的 `markdown` 方法。我们书写的博客文章内容存在 `Post` 的 `body` 属性里，回到我们的详情页视图函数，对 `post` 的 `body` 的值做一下解析，把 Markdown 文本转为 HTML 文本再传递给模板

      ```python
      import markdown
      from django.shortcuts import get_object_or_404, render
      
      from .models import Post
      
      def detail(request, pk):
          article = get_object_or_404(Post, pk=pk)
          article.body = markdown.markdown(article.body,
                                        extensions=[
                                         	'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                        ])
          return render(request, 'detail.html', context={'article': article})
      ```

      这样我们在模板中显示 `{{ post.body }}` 的时候，就不再是原始的 Markdown 文本了，而是解析过后的 HTML 文本。

      [Markdown——入门指南](http://www.jianshu.com/p/1e402922ee32/)

      [Markdown 语法说明 (简体中文版)](http://www.appinn.com/markdown/)

