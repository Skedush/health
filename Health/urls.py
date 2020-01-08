"""Health URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_swagger.views import get_swagger_view
from user.views import UserViewset
from django.urls import path, include

# 配置swagger
schema_view = get_swagger_view(title='Demo API')

urlpatterns = [
    path('user/', include('user.urls')),  # 使用Django REST framework路由系统
    # swagger配置
    path(r'swagger/', schema_view, name="swagger"),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
