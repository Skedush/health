from django.urls import path, include
from .views import TitleViewset
# 使用Django REST framework提供的路由管理
from rest_framework.routers import DefaultRouter
# 使用 viewset 路由
router = DefaultRouter()
# 注册user路由
router.register(r'title', TitleViewset)

urlpatterns = [
    path('', include(router.urls)),  # 使用Django REST framework路由系统

]
