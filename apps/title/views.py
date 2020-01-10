from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from .models import Title

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializers import TitleSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class TitleViewset(ModelViewSet):
    '''
    修改局部数据
    create:  创建用户
    retrieve:  检索某个用户
    update:  更新用户
    destroy:  删除用户
    list:  获取用户列表
    '''
    # authentication是用户认证
    authentication_classes = (JSONWebTokenAuthentication,)
    # permission是权限验证 IsAuthenticated必须登录用户 IsOwnerOrReadOnly必须是当前登录的用户
    # 判断是否登陆
    permission_classes = [IsAuthenticated]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    # drf 过滤&搜索&排序
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    # 搜索
    search_fields = ('title_name', 'user',)
    # 过滤
    filter_fields = ('is_delete',)
    # 排序
    ordering_fields = ('updated', 'created',)
