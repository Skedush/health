from rest_framework import serializers
from .models import Category
import time
import datetime


class CategorySerializer(serializers.ModelSerializer):

    is_delete = serializers.HiddenField(
        default=False)

    class Meta:
        model = Category
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'name', 'is_delete')  # 指定序列化的字段
