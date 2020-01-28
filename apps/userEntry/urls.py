from django.urls import path, include
from .views import EntryInfoViewset, UserEntryViewset
# 使用Django REST framework提供的路由管理
from rest_framework.routers import DefaultRouter
# 使用 viewset 路由
router = DefaultRouter()
# 注册user路由
router.register(r'entryInfo', EntryInfoViewset)
router.register(r'userEntry', UserEntryViewset)

urlpatterns = [
    path('', include(router.urls)),  # 使用Django REST framework路由系统

]
