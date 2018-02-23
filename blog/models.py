from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')  # 必选参数max_length
    content = models.TextField(null=True)  # 没有必选参数

    def __str__(self):
        return self.title
