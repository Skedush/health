# Base类，将增删改查方法重写
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .response import BaseResponse
from rest_framework import filters
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend


class CustomViewBase(viewsets.ModelViewSet):
    # pagination_class = LargeResultsSetPagination
    # filter_class = ServerFilter
    queryset = ''
    serializer_class = ''
    permission_classes = ()
    filter_fields = ()
    search_fields = ()
    filter_backends = (rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter,)
# 创建对象

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return BaseResponse(data=serializer.data, msg="创建成功", code=201, success=True, status=status.HTTP_201_CREATED, headers=headers)

# 获取列表
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return BaseResponse(data=serializer.data, code=200, success=True, msg="success", status=status.HTTP_200_OK)

# 获取详情
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return BaseResponse(data=serializer.data, code=200, success=True, msg="success", status=status.HTTP_200_OK)

# 更新数据
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return BaseResponse(data=serializer.data, msg="更新成功", success=True, code=200, status=status.HTTP_200_OK)

# 删除数据
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete = True
        self.perform_update(instance)
        return BaseResponse(data=[], code=204, success=True, msg="删除成功", status=status.HTTP_204_NO_CONTENT)


class CustomRetrieveModelMixin(
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return BaseResponse(data=serializer.data, code=200, success=True, msg="success", status=status.HTTP_200_OK)
