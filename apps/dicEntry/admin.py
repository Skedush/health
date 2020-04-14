from django.contrib import admin
from .models import Entry,Entryship
from django.contrib.admin import widgets

# 多对多关联表中有多个外键
class EntrysInlineAdmin(admin.TabularInline):
    model = Entryship
    #指定外键
    fk_name = 'from_entry'
    extra=3


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):   
    list_display=('title','remark','category','sort','关联条目')

    fieldsets = (
        (None, {'fields': ('category', 'title','remark','sort')}),
    )
    inlines = (EntrysInlineAdmin,)
    # 添加多对多字段 这里是关键
    def 关联条目(self,obj):
        print(obj.entrys.all())
        return [item.title for item in obj.entrys.all()]
    

