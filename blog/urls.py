from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views import static

from .views import *

urlpatterns = [
    path('', guidance, name='guidance'),
    path('list/', article_list, name='index'),
    path('full/width/', full_width, name='full_width'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('detail/<int:pk>/', article_detail, name='detail'),
    path('archives/<int:year>/<int:month>/', archive, name='archive'),
    path('categories/<int:pk>/', category, name='category'),
    path('tags/<int:pk>/', tag, name='tag'),
    re_path('^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]

handler404 = 'blog.views.page_not_found'
# handler500 = 'index.views.page_error'