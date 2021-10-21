from django.db import models
from django.contrib.auth.models import AbstractUser

# 用户表对象 即 用户表模型


class User(AbstractUser):
    gender_type_choices = (
        ('0', '女'),
        ('1', '男'),
    )

    phone = models.CharField(max_length=11, null=True,
                             blank=True, verbose_name='用户手机号')
    # 字符串类型，开发中并没有使用加密算法，需要上线时可以再加入加密算法
    gender = models.CharField(
        max_length=2, default='1', choices=gender_type_choices,  verbose_name='性别')
    # 时间类型 auto_now_add为添加时的时间，更新对象时不会有变动。
    date_updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # boll类型
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    is_title = models.BooleanField(default=False, verbose_name='修改标题')
    is_vip = models.BooleanField(default=False, verbose_name='会员')

    class Meta:
        db_table = 'h_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        ordering = ['-id']
