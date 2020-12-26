from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="分类")

    def __str__(self):
        return self.category_name


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    category = models.ForeignKey(Category, on_delete=models.CASCADE())
    image = models.ImageField(upload_to="media/upload/", null=True, verbose_name="图片")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_datetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.title
