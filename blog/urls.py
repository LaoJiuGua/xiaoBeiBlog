from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views import static

from .feeds import AllPostsRssFeed
from .views import *

urlpatterns = [
    path('', guidance, name='guidance'),
    path('list/', IndexView.as_view(), name='index'),
    path('full/width/', full_width, name='full_width'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', ArchiveView.as_view(), name='archive'),
    path('categories/<int:pk>/', CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', TagView.as_view(), name='tag'),
    re_path('^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    path('all/rss/', AllPostsRssFeed(), name='rss'),
    path('search/', search, name='search'),
]

handler404 = 'blog.views.page_not_found'
# handler500 = 'index.views.page_error'