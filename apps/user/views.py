from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from .models import User

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from utils.customViewBase import CustomViewBase
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from utils.permissions import IsOwnerOrReadOnly
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils.JWTAuthentication import JWTAuthentication


class UserViewset(CustomViewBase):
    '''
    修改局部数据
    create:  创建用户
    retrieve:  检索某个用户
    update:  更新用户
    destroy:  删除用户
    list:  获取用户列表
    '''
    # authentication是用户认证
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission是权限验证 IsAuthenticated必须登录用户 IsOwnerOrReadOnly必须是当前登录的用户
    # 判断是否登陆
    permission_classes_by_action = {'create': [AllowAny],
                                    'list': [IsAdminUser],
                                    'partial_update': [IsOwnerOrReadOnly],
                                    'retrieve': [IsOwnerOrReadOnly],
                                    'destroy': [IsAdminUser], }
    queryset = User.objects.order_by('-id')

    serializer_class = UserSerializer
    # drf 过滤&搜索&排序
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    # 搜索
    search_fields = ('username', 'phone', 'email',)
    # 过滤
    filter_fields = ('gender',)
    # 排序
    ordering_fields = ('updated', 'created',)

    def perform_create(self, serializer):
        if self.request and self.request.data['title']:
            title = self.request.data['title']
        serializer.save(title=title)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


#     def get_object(self, queryset=None):
#         obj = super().get_object(queryset=queryset)
#         if obj.author != self.request.user:
#             raise Http404()
#         return obj
