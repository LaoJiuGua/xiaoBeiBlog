from django.shortcuts import render

# Create your views here.


def index(request):
    """ 首页 """
    return render(request, 'index.html')


def full_width(request):
    """ 博客 """
    return render(request, 'full-width.html')


def about(request):
    """ 联系 """
    return render(request, 'about.html')


def contact(request):
    """ 关于 """
    return render(request, 'contact.html')


def single(request):
    """ 详情 """
    return render(request, 'single.html')