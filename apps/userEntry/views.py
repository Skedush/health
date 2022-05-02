from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from .models import EntryInfo, UserEntry, UserEntryOfEntry

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from utils.customViewBase import CustomViewBase, CustomRetrieveModelMixin
from .serializers import EntryInfoSerializer, EntryInfoListSerializer, UserEntrySerializer, ResultUserEntrySerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication, BaseJSONWebTokenAuthentication
from utils.JWTAuthentication import JWTAuthentication
from utils.response import BaseResponse
from rest_framework import status
from utils.DrfPaginate import DrfPaginate

# from .titleFilter import TitleFilter


class EntryInfoViewset(CustomViewBase):
    '''
    修改局部数据
    create:  创建分类
    retrieve:  检索某个分类
    update:  更新分类
    destroy:  删除分类
    list:  获取分类列表
    '''
    # authentication是用户认证
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = [JSONWebTokenAuthentication, ]

    # permission是权限验证 IsAuthenticated必须登录用户 IsOwnerOrReadOnly必须是当前登录的用户
    # 判断是否登陆
    # permission_classes = [IsAuthenticated]

    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [IsAuthenticated],
                                    'update': [IsAuthenticated],
                                    'retrieve': [AllowAny],
                                    'destroy': [IsAuthenticated], }
    queryset = EntryInfo.objects.all()
    serializer_class = EntryInfoSerializer
    # drf 过滤&搜索&排序
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    # 搜索
    search_fields = ('title', 'user', 'category')
    # 过滤
    # filter_fields = ('is_delete',)
    # filter_class = TitleFilter
    # 排序
    ordering_fields = ('id')

    def get_serializer_class(self):
        if self.action == "list":
            return EntryInfoListSerializer
        return EntryInfoSerializer

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        # if self.request.user.is_superuser:
        #     return EntryInfo.objects.filter(is_delete=False)
        # else:
        if self.action == 'retrieve':
            return EntryInfo.objects.filter()
        return EntryInfo.objects.filter(user=self.request.user, is_delete=False)


class UserEntryViewset(CustomViewBase):
    '''
    修改局部数据
    create:  创建分类
    retrieve:  检索某个分类
    update:  更新分类
    destroy:  删除分类
    list:  获取分类列表
    '''
    # authentication是用户认证
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = [JSONWebTokenAuthentication, ]

    # permission是权限验证 IsAuthenticated必须登录用户 IsOwnerOrReadOnly必须是当前登录的用户
    # 判断是否登陆
    # permission_classes = [IsAuthenticated]
    permission_classes_by_action = {'create': [AllowAny],
                                    'list': [IsAuthenticated],
                                    'update': [IsAuthenticated],
                                    'retrieve': [IsAuthenticated],
                                    'destroy': [IsAuthenticated], }
    queryset = UserEntry.objects.all()
    serializer_class = UserEntrySerializer
    pagination_class = DrfPaginate
    # drf 过滤&搜索&排序
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    # 搜索
    search_fields = ('name', 'phone', 'remark')
    # 过滤
    filter_fields = ('entry_info',)
    # filter_class = TitleFilter
    # 排序
    # ordering_fields = ('-id')

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        return UserEntry.objects.filter(is_delete=False)


class ResultUserEntryViewset(CustomRetrieveModelMixin):
    '''
    修改局部数据
    create:  创建分类
    retrieve:  检索某个分类
    update:  更新分类
    destroy:  删除分类
    list:  获取分类列表
    '''
    # authentication是用户认证
    authentication_classes = [JWTAuthentication]
    # authentication_classes = [JSONWebTokenAuthentication, ]

    # permission是权限验证 IsAuthenticated必须登录用户 IsOwnerOrReadOnly必须是当前登录的用户
    # 判断是否登陆
    permission_classes = [IsAuthenticated]
    queryset = UserEntry.objects.prefetch_related('entryship__entrys__category').all().order_by('-id')
    serializer_class = ResultUserEntrySerializer
    # drf 过滤&搜索&排序
    # 排序
    ordering_fields = ('-id')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return BaseResponse(data=serializer.data, code=200, success=True, msg="success", status=status.HTTP_200_OK)
