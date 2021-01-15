from django.urls import path

from . import views

urlpatterns = [
    path('comment/<int:pk>', views.comment, name='comment'),
]