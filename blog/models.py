from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')  # 必选参数max_length
    content = models.TextField(null=True)  # 没有必选参数
    # pub_time = models.DateTimeField(auto_now=True)  # auto_now意思是创建对象时自动设置为当前时间
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        """Python语法，用于显示这个类的实例对象打印出来的效果"""
        return self.title
