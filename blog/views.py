from django.shortcuts import render
from django.http import HttpResponse

from . import models


# def index(request):
#     return HttpResponse("Hello, World!")

def index(request):
    # article = models.Arcticle.objects.get(pk=1)  # 获取主键值为1的文章
    articles = models.Arcticle.objects.all()  # 获取所有文章
    return render(request, 'blog/index.html', {'articles': articles})  # 第二个参数是相对templates目录的路径


def article_page(request, article_id):
    article = models.Arcticle.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})
