from rest_framework import serializers
from .models import Entry
import time
import datetime


class DicEntrySerializer(serializers.ModelSerializer):

    is_delete = serializers.HiddenField(
        default=False)

    class Meta:
        model = Entry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'title', 'content', 'is_delete')  # 指定序列化的字段


class EntrySerializer(serializers.ModelSerializer):

    is_delete = serializers.HiddenField(
        default=False)

    entryIds = DicEntrySerializer(many=True)

    class Meta:
        model = Entry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'title', 'content', 'entryIds', 'is_delete')  # 指定序列化的字段
