# Generated by Django 2.1 on 2020-01-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0002_title_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='逻辑删除'),
        ),
    ]