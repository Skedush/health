# Generated by Django 3.0.8 on 2021-01-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0002_title_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='title_name',
            field=models.CharField(max_length=20, verbose_name='标题名称'),
        ),
    ]
