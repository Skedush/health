from django.db import models

# Create your models here.


class Entry(models.Model):

    id = models.AutoField(primary_key=True)

    category = models.ForeignKey(
        'category.Category', null=True, on_delete=models.SET_NULL, verbose_name='分类id外键')

    title = models.ForeignKey('title.Title', null=True,
                              on_delete=models.SET_NULL)

    content = models.CharField(max_length=255, null=True,
                               blank=True, verbose_name='条目内容')

    # 时间类型 auto_now_add为添加时的时间，更新对象时不会有变动。
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 时间类型 auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # boll类型
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    entry = models.ManyToManyField(
        to='self', symmetrical=False, related_name='ship')

    class Meta:
        db_table = 'h_entry'
        verbose_name = '条目信息表'
        verbose_name_plural = verbose_name


# class EntryShip(models.Model):

#     id = models.AutoField(primary_key=True)

#     category = models.ForeignKey(
#         'category.Category', null=True, on_delete=models.SET_NULL, verbose_name='分类id外键')

#     entry = models.ForeignKey(Entry, null=True,
#                               on_delete=models.SET_NULL, verbose_name='条目id外键')

#     entry_ship = models.ForeignKey(Entry, null=True,
#                                    on_delete=models.SET_NULL, verbose_name='条目关联id外键')

#     class Meta:
#         db_table = 'h_entry_ship'
#         verbose_name = '条目信息自关联表'
#         verbose_name_plural = verbose_name
