"""
Created on 2018/2/22
@Author: Jeff Yang
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index),  # ^$分别限制开头和结尾，即限定为空
    url(r'^index/$', views.index),  # 限制index，注意加一个‘/’，否则访问“http://localhost:8000/blog/index/”会出现404
    # 把匹配到的数字以article_id作为组名，组名必须和响应函数的参数名一致，否则会报错
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
]
