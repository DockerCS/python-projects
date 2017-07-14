from django.db import models
from ..user.models import User, Author

# Article模型的管理器
class ArticleManager(models.Manager):
    def query_by_column(self, column_id):
        query = self.get_queryset().filter(column_id=column_id)

    def query_by_user(self, user_id):
        user = User.objects.get(id=user_id)
        article_list = user.article_set.all()
        return article_list

    def query_by_polls(self):
        query = self.get_queryset().order_by('poll_num')
        return query

    def query_by_time(self):
        query = self.get_queryset().order_by('-created_time')
        return query

    def query_by_keyword(self, keyword):
        query = self.get_queryset().filter(title__contains=keyword)
        return query


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
    user = models.ManyToManyField(User, blank=True)
    poll_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    category = models.ForeignKey(Category)  # 文章的分类

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'

    objects = ArticleManager()


# 评论
class Comment(models.Model):
    content = models.TextField()  # 评论内容
    created_time = models.DateTimeField(auto_now_add=True, null=True)  # 评论时间
    poll_num = models.IntegerField(default=0)  # 点赞次数
    user = models.ForeignKey(User)
    parent_comment = models.ForeignKey('Comment', null=True, blank=True)
    article = models.ForeignKey(Article, null=True)

    def __str__(self):
        return self.content


# 点赞
class Poll(models.Model):
    user = models.ForeignKey(User, null=True)
    article = models.ForeignKey(Article, null=True)
    comment = models.ForeignKey(Comment, null=True)
# Create your models here.

