from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy

admin.AdminSite.site_header = '填表管理系统'
admin.AdminSite.site_title = '填表管理系统'

class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (gettext_lazy('Personal info'), {'fields': ('first_name',
                                                    'last_name', 'email', 'phone', 'gender')}),
        (gettext_lazy('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_delete',
                                                  'groups', 'user_permissions')}),
        (gettext_lazy('Important dates'), {
         'fields': ('last_login', 'date_joined')}),
    )
    
    list_per_page = 10
    ordering = ('-id',)

    


# Register your models here.
admin.site.register(User, UserProfileAdmin)
