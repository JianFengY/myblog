from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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


def edit_page(request, article_id):
    if str(article_id) == '0':  # ID是从1开始的，所以新建文章时传入0
        return render(request, 'blog/edit_page.html')
    article = models.Arcticle.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')  # 也可以用request.POST['title']，这里的TITLE为默认值
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        models.Arcticle.objects.create(title=title, content=content)
        # articles = models.Arcticle.objects.all()
        # return render(request, 'blog/index.html', {'articles': articles})
        # 新建博客成功后会跳转到首页，这时浏览器里地址还是指向刚才的提交表单地址http://localhost:8000/blog/edit/action/
        # 这时候刷新页面，会再多添加一条数据。
        # 改成以下语句重定向
        return HttpResponseRedirect('/blog/index')
    article = models.Arcticle.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})
