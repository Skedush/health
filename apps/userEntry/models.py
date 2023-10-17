from django.db import models
from django.conf import settings

# 用户表对象 即 用户表模型


class EntryInfo(models.Model):

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, on_delete=models.SET_NULL)

    category = models.ForeignKey(
        'category.Category', null=True, on_delete=models.SET_NULL)

    title = models.ForeignKey('title.Title', null=True,
                              on_delete=models.SET_NULL)

    # 时间类型 auto_now_add为添加时的时间，更新对象时不会有变动。
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 时间类型 auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # boll类型
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'h_entry_info'
        verbose_name = '用户创建条目信息表'
        verbose_name_plural = verbose_name


class UserEntry(models.Model):
    gender_type_choices = (
        ('0', '女'),
        ('1', '男'),
    )
    id = models.AutoField(primary_key=True)

    entry_info = models.ForeignKey(
        'EntryInfo', null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=20, null=True,
                            blank=True, verbose_name='填写表单人员姓名')
    gender = models.CharField(
        max_length=2, default='1', choices=gender_type_choices,  verbose_name='性别')
    height = models.CharField(null=True, max_length=10,
                              blank=True, verbose_name='身高cm')

    weight = models.CharField(null=True, max_length=10,
                              blank=True, verbose_name='体重kg')

    age = models.CharField(null=True, max_length=10,
                           blank=True, verbose_name='年龄')
    address = models.CharField(max_length=255, null=True,
                               blank=True, verbose_name='地址')

    waistline = models.CharField(null=True, max_length=10,
                                 blank=True, verbose_name='腰围cm')

    systolic_pressure = models.CharField(null=True, max_length=20,
                                         blank=True, verbose_name='收缩压mmHg')

    diastolic_pressure = models.CharField(null=True, max_length=20,
                                          blank=True, verbose_name='舒张压mmHg')

    blood_sugar = models.CharField(null=True, max_length=20,
                                   blank=True, verbose_name='血糖mmol/L')

    remark=models.TextField(max_length=10240, null=True,
                              blank=True, verbose_name='备注')

    suggestion = models.TextField(max_length=10240, null=True,
                                  blank=True, verbose_name='建议')

    phone = models.CharField(max_length=11, null=True,
                             blank=True, verbose_name='用户手机号')

    # 时间类型 auto_now_add为添加时的时间，更新对象时不会有变动。
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 时间类型 auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # boll类型
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    entryship = models.ManyToManyField(
        'dicEntry.Entry', through='UserEntryOfEntry')

    class Meta:
        db_table = 'h_user_entry'
        verbose_name = '用户选择条目信息表'
        verbose_name_plural = verbose_name
        ordering = ['-id']


class UserEntryOfEntry(models.Model):

    id = models.AutoField(primary_key=True)

    user_entry = models.ForeignKey(UserEntry, on_delete=models.CASCADE)

    entry = models.ForeignKey(
        'dicEntry.Entry', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'h_userentry_entry'
        verbose_name = '用户选择条目信息表'
        verbose_name_plural = verbose_name
