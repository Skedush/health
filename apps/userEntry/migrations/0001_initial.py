# Generated by Django 2.1 on 2020-01-24 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('title', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dicEntry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='title.Title')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户创建条目信息表',
                'verbose_name_plural': '用户创建条目信息表',
                'db_table': 'h_entry_info',
            },
        ),
        migrations.CreateModel(
            name='UserEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='填写表单人员姓名')),
                ('gender', models.CharField(choices=[('0', '女'), ('1', '男')], default='1', max_length=2, verbose_name='性别')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='身高cm')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='体重kg')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='地址')),
                ('waistline', models.IntegerField(blank=True, null=True, verbose_name='腰围cm')),
                ('systolic_pressure', models.IntegerField(blank=True, null=True, verbose_name='收缩压mmHg')),
                ('diastolic_pressure', models.IntegerField(blank=True, null=True, verbose_name='舒张压mmHg')),
                ('blood_sugar', models.IntegerField(blank=True, null=True, verbose_name='血糖mmol/L')),
                ('remark', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='用户手机号')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('entry_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userEntry.EntryInfo')),
            ],
            options={
                'verbose_name': '用户选择条目信息表',
                'verbose_name_plural': '用户选择条目信息表',
                'db_table': 'h_user_entry',
            },
        ),
        migrations.CreateModel(
            name='UserEntryOfEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dicEntry.Entry')),
                ('user_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userEntry.UserEntry')),
            ],
            options={
                'verbose_name': '用户选择条目信息表',
                'verbose_name_plural': '用户选择条目信息表',
                'db_table': 'h_userentry_entry',
            },
        ),
        migrations.AddField(
            model_name='userentry',
            name='entryship',
            field=models.ManyToManyField(through='userEntry.UserEntryOfEntry', to='dicEntry.Entry'),
        ),
    ]
