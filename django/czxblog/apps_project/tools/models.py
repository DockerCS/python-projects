from django.db import models
from django.contrib.contenttypes.models import ContentType  # 引用ContentType相关模块
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User  # 引用系统自带的用户模型

"""阅读统计"""
class View(models.Model):
    """阅读明细记录"""
    # ContentType设置
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field="content_type",
        fk_field="object_id"
    )

    # 普通字段
    # 记录IP地址
    ip_address = models.CharField(max_length=15)

    # 记录User，这里可能没有登录用户，所以要允许为空
    user = models.ForeignKey(User, blank=True, null=True)

    # 阅读的时间
    view_time = models.DateTimeField(auto_now=True)

class ViewNum(models.Model):
    """阅读数量记录"""
    # ContentType设置
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field="content_type",
        fk_field="object_id"
    )

    # 普通字段，阅读总数量
    view_num = models.IntegerField(default=0)

    def __str____(self):
        return u'<%s:%s> %s' % (self.content_type, self.object_id, self.view_num)


"""点赞统计"""
class Poll():
    """点赞明细记录"""
    pass

class PollNum():
    """点赞数目记录"""
    pass
