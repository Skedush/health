# Generated by Django 2.0.6 on 2020-01-02 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='userid',
            new_name='user',
        ),
    ]
