from django.contrib import admin
from .models import Title

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):   
    #设置哪些字段可以点击进入编辑界面
    list_display=('title_name','user','created')
    ordering = ('-id',)

