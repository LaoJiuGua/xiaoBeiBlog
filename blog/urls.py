from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('full/width/', full_width, name='full_width'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('single/', single, name='single'),
]