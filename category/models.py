from django.db import models

# 用户表对象 即 用户表模型


class Category(models.Model):
    id = models.AutoField(primary_key=True)

    # 字符串类型，max_length表示最大长度255，verbose_name表示备注的字段中文名
    category_name = models.CharField(max_length=100, verbose_name='分类名称')
    # 时间类型 auto_now_add为添加时的时间，更新对象时不会有变动。
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 时间类型 auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # boll类型
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'h_category'
        verbose_name = '分类表'
        verbose_name_plural = verbose_name
