from django.db import models
from django.conf import settings

# 用户表对象 即 用户表模型


class Title(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    # 字符串类型，max_length表示最大长度255，verbose_name表示备注的字段中文名
    title_name = models.CharField(max_length=20, verbose_name='用户名')
    # 时间类型 auto_now_add为添加时的时间，更新对象时不会有变动。
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 时间类型 auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'h_title'
        verbose_name = '用户标题表'
        verbose_name_plural = verbose_name
