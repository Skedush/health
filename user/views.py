from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from .models import User

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer


class UserViewset(ModelViewSet):
    '''
    修改局部数据
    create:  创建用户
    retrieve:  检索某个用户
    update:  更新用户
    destroy:  删除用户
    list:  获取用户列表
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # drf 过滤&搜索&排序
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    # 搜索
    search_fields = ('username', 'phone', 'email',)
    # 过滤
    filter_fields = ('gender',)
    # 排序
    ordering_fields = ('updated', 'created',)
