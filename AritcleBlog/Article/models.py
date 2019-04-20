from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

"""
 Title
         Authoer
         Time
         ContentC:\Python35\Scripts
         Description
         picture
"""
class Article(models.Model):
    title = models.CharField(max_length = 32,verbose_name = "文章标题")
    author = models.CharField(max_length = 32,verbose_name = "文章作者")
    time = models.CharField(verbose_name = "发表日期")
    description = RichTextUploadingField(verbose_name = "文章描述")
    content = RichTextUploadingField(verbose_name = "文章内容")
    picture = models.ImageField(upload_to = "image")

    def __str__(self):
        return  self.title