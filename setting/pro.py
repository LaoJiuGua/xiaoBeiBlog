from .base import *

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'HOST': '139.159.245.251',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'qq1363698962'
    }
}