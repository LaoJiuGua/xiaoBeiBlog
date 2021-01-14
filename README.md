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

  - 文章表

    | 文章ID | 标题  | 正文 | 作者 | 分类   | 标签   | 发表时间  |
    | ------ | ----- | ---- | ---- | ------ | ------ | --------- |
    | 1      | Ttile | Text | 鲁迅 | Django | Python | 2021-1-14 |

  - 分类表

    | 分类ID | 分类名 |
    | ------ | ------ |
    | 1      | Django |

  - 标签表

    | 标签ID | 标签名 |
    | :----- | ------ |
    | 1      | Python |

    