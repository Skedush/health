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
        fields = ('id', 'title', 'remark', 'is_delete')  # 指定序列化的字段


class EntrySerializer(serializers.ModelSerializer):

    is_delete = serializers.HiddenField(
        default=False)

    entry = DicEntrySerializer(many=True)
    # entry = serializers.PrimaryKeyRelatedField(
    # many=True, queryset=Entry.objects.all())

    class Meta:
        model = Entry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'title', 'remark', 'entry', 'is_delete')  # 指定序列化的字段

    # def create(self, validated_data):
    #     print('qweqweq')
    #     return Entry.objects.create(**validated_data)
