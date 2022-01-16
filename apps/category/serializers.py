from rest_framework import serializers
from .models import Category
from dicEntry.models import Entry
# from dicEntry.serializers import CategoryEntrySerializer
import time
import datetime


class CategorySerializer(serializers.ModelSerializer):

    is_delete = serializers.HiddenField(
        default=False)

    class Meta:
        model = Category
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'name', 'is_delete', 'link',
                  'child_link', 'show_count', 'has_user_rule', 'protocol')  # 指定序列化的字段


class CategoryEntrySerializer(serializers.ModelSerializer):
    # count = serializers.IntegerField()

    class Meta:
        model = Entry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'title', 'remark')  # 指定序列化的字段


class ResultCategorySerializer(serializers.ModelSerializer):

    entrys = CategoryEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'name',  'entrys')  # 指定序列化的字段
