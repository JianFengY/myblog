from django.contrib import admin
from blog.models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    #属性的值是一个包含字符串格式的字段名的tuple或list。建议使用tuple，因为tuple不可变，比较安全。
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)  # tuple只有一个元素时记得加个逗号


admin.site.register(Article, ArticleAdmin)
