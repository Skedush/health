from rest_framework import serializers
from .models import Entry, Entryship
from category.models import Category
from category.serializers import CategorySerializer
import time
import datetime


class DicEntrySerializer(serializers.ModelSerializer):

    is_delete = serializers.HiddenField(
        default=False)
    category = CategorySerializer()

    class Meta:
        model = Entry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'title', 'remark', 'is_delete',
                  'sort', 'category')  # 指定序列化的字段

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
    category = CategorySerializer(read_only=True)
    category_Id = serializers.SlugRelatedField(write_only=True,
                                               slug_field="id", queryset=Category.objects.all())

    entrys = DicEntrySerializer(many=True, read_only=True)
    entry_Ids = serializers.SlugRelatedField(
        many=True, write_only=True, slug_field="id", queryset=Entry.objects.all())

    # entrys = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Entry.objects.all())

    class Meta:
        model = Entry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'title', 'remark', 'entrys',
                  'is_delete', 'category', 'sort', 'category_Id', 'entry_Ids')  # 指定序列化的字段

    def validate(self, attrs):
        print(attrs)
        # del attrs['entry_Ids']
        return attrs

    def create(self, validated_data):
        entry_Ids = validated_data.pop('entry_Ids')
        category_Id = validated_data.pop('category_Id')
        entry = Entry.objects.create(**validated_data, category=category_Id)
        for entry_Id in entry_Ids:
            # entry = Entryship.objects.filter(id=entry_Ids)
            Entryship.objects.create(
                from_entry=entry, to_entry=entry_Id, category=entry_Id.category)
        return entry
