# Generated by Django 2.1 on 2020-02-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userEntry', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userentry',
            options={'ordering': ['-id'], 'verbose_name': '用户选择条目信息表', 'verbose_name_plural': '用户选择条目信息表'},
        ),
        migrations.AlterField(
            model_name='userentry',
            name='age',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='blood_sugar',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='血糖mmol/L'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='diastolic_pressure',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='舒张压mmHg'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='height',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='身高cm'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='systolic_pressure',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='收缩压mmHg'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='waistline',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='腰围cm'),
        ),
        migrations.AlterField(
            model_name='userentry',
            name='weight',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='体重kg'),
        ),
    ]
