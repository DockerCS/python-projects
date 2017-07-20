from django.db import models

# 用户
class User(models.Model):
    name = models.CharField(max_length=30)  # 用户姓名
    # password = models.CharField(max_length=30)  # 用户密码
    profile = models.CharField(max_length=250)  # 用户介绍

    def __str__(self):
        return self.name


# 作者
class Author(models.Model):
    name = models.CharField(max_length=30)  # 作者姓名
    profile = models.CharField(max_length=250)  # 作者介绍

    def __str__(self):
        return self.name

# Create your models here.
