from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('', article_list, name='index'),
    path('full/width/', full_width, name='full_width'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('detail/<int:pk>/', article_detail, name='detail'),
]