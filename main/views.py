from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def blog(request):
    return render(request, 'main/blog.html')


def contact(request):
    return render(request, 'main/basic.html', {'cont': ['test']})


def shop(request):
    return render(request, 'main/shop.html')