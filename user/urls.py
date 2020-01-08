from django.urls import path, include
from .views import UserViewset
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
# 使用Django REST framework提供的路由管理
from rest_framework.routers import DefaultRouter
# 使用 viewset 路由
router = DefaultRouter()
# 注册user路由
router.register(r'userapi', UserViewset)

urlpatterns = [
    path('', include(router.urls)),  # 使用Django REST framework路由系统
    path(r'login', obtain_jwt_token),
    path(r"refresh", refresh_jwt_token),

]
