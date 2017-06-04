from django.db import models


# 用户
class User(models.Model):
    name = models.CharField(max_length=30)  # 用户姓名
    profile = models.CharField(max_length=250)  # 用户介绍

    def __str__(self):
        self.name


# 作者
class Author(models.Model):
    name = models.CharField(max_length=30)  # 作者姓名
    profile = models.CharField(max_length=250)  # 作者介绍

    def __str__(self):
        self.name


# 文章的分类
class Classification(models.Model):
    name = models.CharField(max_length=30)  # 分类名称
    profile = models.CharField(max_length=250)  # 分类介绍


    def __str__(self):
        self.name


# 文章
class Artical(models.Model):
    title = models.CharField(max_length=30)  # 文章题目
    content = models.TextField()  # 文章内容
# Create your models here.
