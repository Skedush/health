from django.contrib import admin
from .models import Entry, Entryship

# 多对多关联表中有多个外键

class EntrysInlineAdmin(admin.TabularInline):
    model = Entryship
    # 指定外键
    fk_name = 'from_entry'
    raw_id_fields = ('to_entry',)
    extra = 3


class EntryListFilter(admin.SimpleListFilter):
    title = (u'关联条目')
    parameter_name = 'entrys__title'

    def lookups(self, request, model_admin):
        qs = model_admin.model.objects.all()
        ret = []
        # or might be able to use yeild here
        for entry in qs.exclude(category__in=[3, 6, 7]):
            ret.append((entry.title, entry.title))
        return ret

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(entrys__title=self.value())
        else:
            return queryset


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'remark', 'category', 'sort', '关联条目')
    list_display_links = ('title',)
    fieldsets = (
        (None, {'fields': ('category', 'title', 'remark', 'sort')}),
    )
    list_per_page = 500
    search_fields = ['title']
    list_filter = ['category', EntryListFilter]
    inlines = (EntrysInlineAdmin,)
    # 添加多对多字段 这里是关键

    def 关联条目(self, obj):
        return [item.title for item in obj.entrys.all()]
