from django.contrib import admin
from .models import Category

@admin.register(Category)
class TitleAdmin(admin.ModelAdmin):   
    #设置哪些字段可以点击进入编辑界面
    list_display=('name','updated','created','is_delete')
    ordering = ('-id',)

