import os
import pathlib
import random
import sys
from datetime import timedelta

import django
import faker
from django.utils import timezone

# 将项目根目录添加到 Python 的模块搜索路径中
# back = os.path.dirname
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xiaoBeiBlog.settings")
    django.setup()

    from blog.models import Category,Tag,Post
    from comments.models import Comment
    from django.contrib.auth.models import User

    print('-----清除旧数据-----')
    Post.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()
    Comment.objects.all().delete()
    User.objects.all().delete()
    print('-----清除旧数据完成-----')

    print('-----创建新后台管理员-----')
    user = User.objects.create_superuser('admin', '1113855149@qq.com', '123456')

    category_list = ['Python学习笔记', '开源项目', '工具资源', '程序员生活感悟', 'test category']
    tag_list = ['django', 'Python', 'Pipenv', 'Docker', 'Nginx', 'Elasticsearch', 'Gunicorn', 'Supervisor', 'test tag']
    a_year_ago = timezone.now() - timedelta(days=365)

    print('-----添加分类和标签-----')
    for cate in category_list:
        Category.objects.create(name=cate)

    for tag in tag_list:
        Tag.objects.create(name=tag)

    print('添加Markdown文件模型')
    Post.objects.create(
        title='Markdown 与代码高亮测试',
        body=pathlib.Path(BASE_DIR).joinpath('scripts', 'md.sample').read_text(encoding='utf-8'),
        category=Category.objects.create(name='Markdown测试'),
        author=user,
    )

    print('创建今年和去年的文章')
    fake = faker.Faker('zh_CN')  # English
    for _ in range(100):
        tags = Tag.objects.order_by('?')
        tag1 = tags.first()
        tag2 = tags.last()
        cate = Category.objects.order_by('?').first()
        created_time = fake.date_time_between(start_date='-1y', end_date="now",
                                              tzinfo=timezone.get_current_timezone())
        post = Post.objects.create(
            title=fake.sentence().rstrip('.'),
            body='\n\n'.join(fake.paragraphs(10)),
            created_time=created_time,
            category=cate,
            author=user,
        )
        post.tags.add(tag1, tag2)
        post.save()

        print('添加评论')
        for post in Post.objects.all()[:20]:
            post_created_time = post.created_time
            delta_in_days = '-' + str((timezone.now() - post_created_time).days) + 'd'
            for _ in range(random.randrange(3, 15)):
                Comment.objects.create(
                    name=fake.name(),
                    email=fake.email(),
                    url=fake.uri(),
                    text=fake.paragraph(),
                    created_time=fake.date_time_between(
                        start_date=delta_in_days,
                        end_date="now",
                        tzinfo=timezone.get_current_timezone()),
                    post=post,
                )

        print('done!')
