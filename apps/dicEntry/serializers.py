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
        fields = ('id', 'title', 'remark', 'is_delete', 'category')  # 指定序列化的字段

    # def to_representation(self, value):
    #     print('value: ', value);
    #     entrys = []
    #     for entryId in value:
    #         entry = Entry.objects.filter(id=entryId)
    #         entrys.append(entry)
    #     return entrys



class EntrySerializer(serializers.ModelSerializer):

    is_delete = serializers.HiddenField(
        default=False)

    entrys = DicEntrySerializer(many=True)
    # entrys = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Entry.objects.all())

    class Meta:
        model = Entry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'title', 'remark', 'entrys',
                  'is_delete', 'category')  # 指定序列化的字段

    # def validate(self, attrs):
    #     print(attrs)
    #     del attrs["entrys"]
    #     return attrs

    # def create(self, validated_data):
    #     entrys_data = validated_data.pop('entrys')
    #     print('entrys_data: ', entrys_data)
    #     entry = Entry.objects.create(**validated_data)
    #     for entry_data in entrys_data:
    #         entry.objects.create(entry=entry, **entry_data)
    #     return entry
    # def create(self, validated_data):
    #     print('qweqweq')
    #     return Entry.objects.create(**validated_data)
