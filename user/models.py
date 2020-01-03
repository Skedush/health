from django.db import models

# 用户表对象 即 用户表模型


class User(models.Model):
    gender_type_choices = (
        ('0', '女'),
        ('1', '男'),
    )
    user_type_choices = (
        ('1', '普通用户'),
        ('2', '超级管理员'),
    )
    id = models.AutoField(primary_key=True)

    # 字符串类型，max_length表示最大长度255，verbose_name表示备注的字段中文名
    username = models.CharField(max_length=20, verbose_name='用户名')
    # 字符串类型
    phone = models.CharField(max_length=11, null=True,
                             blank=True, verbose_name='用户手机号')
    # 邮箱类型，null表示值允许为空 blank表示值可以为空字符串 default表示默认为空字符串
    email = models.EmailField(default='', null=True,
                              blank=True, verbose_name='用户邮箱')
    # 字符串类型，开发中并没有使用加密算法，需要上线时可以再加入加密算法
    password = models.CharField(
        max_length=20, verbose_name='用户密码')
    adminState = models.CharField(
        max_length=2, default='1', choices=user_type_choices,  verbose_name='用户类型')
    # 字符串类型 使用 choices 参数，表示有 0 1 两种选项
    gender = models.CharField(
        max_length=2, default='1', choices=gender_type_choices,  verbose_name='性别')
    # 时间类型 auto_now_add为添加时的时间，更新对象时不会有变动。
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 时间类型 auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # boll类型
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'h_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
