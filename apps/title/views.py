from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from .models import Title

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from utils.customViewBase import CustomViewBase
from .serializers import TitleSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from utils.permissions import IsOwnerOrReadOnly
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication, BaseJSONWebTokenAuthentication
from utils.JWTAuthentication import JWTAuthentication
from utils.response import BaseResponse
from .titleFilter import TitleFilter


class TitleViewset(CustomViewBase):
    '''
    修改局部数据
    create:  创建标题
    retrieve:  检索某个标题
    update:  更新标题
    destroy:  删除标题
    list:  获取标题列表
    '''
    # authentication是用户认证
    authentication_classes = [JWTAuthentication]
    # authentication_classes = [JSONWebTokenAuthentication, ]

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
    # filter_fields = ('is_delete',)
    filter_class = TitleFilter
    # 排序
    ordering_fields = ('updated', 'created',)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Title.objects.filter(is_delete=False)
        else:
            return Title.objects.filter(user=self.request.user, is_delete=False)
