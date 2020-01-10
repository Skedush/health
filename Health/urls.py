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
# from rest_framework_swagger.views import get_swagger_view
from rest_framework_swagger import renderers
from user.views import UserViewset
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.schemas import get_schema_view as get_schema_view_swagger
from drf_yasg import openapi
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

schema_view = get_schema_view(
    openapi.Info(
        title="CMDB API",
        default_version='v1',
        description="资产管理系统API接口文档",
        terms_of_service="https://www.shuaibo.wang/",
        contact=openapi.Contact(email="mail@shuaibo.wang"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# 配置swagger
# schema_view_swagger = get_swagger_view(title='Demo API')
schema_view_swagger = get_schema_view_swagger(title='API', public=True, renderer_classes=[
    renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])

urlpatterns = [
    path('', include('user.urls')),  # 使用Django REST framework路由系统
    path('', include('title.urls')),  # 使用Django REST framework路由系统

    path(r'login', obtain_jwt_token),
    path(r"refresh", refresh_jwt_token),

    path(r'api_doc/', schema_view.with_ui('redoc',
                                          cache_timeout=0), name="CMDB API"),
    # swagger配置
    path(r'swagger/', schema_view_swagger, name="swagger"),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
