from django.db import models


# 用户
class User(models.Model):
    name = models.CharField(max_length=30)  # 用户姓名
    profile = models.CharField(max_length=250)  # 用户介绍

    def __str__(self):
        return self.name


# 作者
class Author(models.Model):
    name = models.CharField(max_length=30)  # 作者姓名
    profile = models.CharField(max_length=250)  # 作者介绍

    def __str__(self):
        return self.name


# 文章的分类
class Category(models.Model):
    name = models.CharField(max_length=30)  # 分类名称
    profile = models.CharField(max_length=250)  # 分类介绍


    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(max_length=200)  # 文章题目
    content = models.TextField()  # 文章内容
    created_time = models.DateTimeField(auto_now_add=True)  # 文章创建时间
    modified_time = models.DateTimeField(auto_now=True)  # 文章修改时间
    Author = models.ForeignKey(Author)  # 文章作者
    category = models.ForeignKey(Category)  # 文章的分类

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_time']


# 评论
class Comment(models.Model):
    content = models.TextField()  # 评论内容
    created_time = models.DateTimeField(auto_now_add=True)  # 评论时间
    poll_number = models.IntegerField(default=0)  # 点赞次数
    user = models.ForeignKey(User)
    parent_comment = models.ForeignKey('Comment')
    article = models.ForeignKey(Article)


    def __str__(self):
        return self.content


# 点赞
class Poll(models.Model):
    user = models.ForeignKey(User, null=True)
    article = models.ForeignKey(Article, null=True)
    comment = models.ForeignKey(Comment, null=True)
# Create your models here.
