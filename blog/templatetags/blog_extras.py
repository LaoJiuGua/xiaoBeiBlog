from django import template

from comments.forms import CommentForm
from ..models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }


@register.inclusion_tag('inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }


@register.inclusion_tag('inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }


@register.inclusion_tag('inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }


@register.inclusion_tag('inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }