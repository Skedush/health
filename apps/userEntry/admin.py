from django.contrib import admin
from .models import EntryInfo


@admin.register(EntryInfo)
class EntryInfoAdmin(admin.ModelAdmin):   
    #设置哪些字段可以点击进入编辑界面
    list_display=('title','category','user')
    ordering = ('-id',)

