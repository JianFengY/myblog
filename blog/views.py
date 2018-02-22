from django.shortcuts import render
from django.http import HttpResponse

from . import models

# def index(request):
#     return HttpResponse("Hello, World!")

def index(request):
    article = models.Arcticle.objects.get(pk=1)
    return render(request, 'blog/index.html', {'article': article})  # 第二个参数是相对templates目录的路径
