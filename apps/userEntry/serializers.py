from rest_framework import serializers
from .models import EntryInfo, UserEntry, UserEntryOfEntry
from dicEntry.models import Entry
from dicEntry.serializers import DicEntrySerializer
import time
import datetime


class EntryInfoSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    is_delete = serializers.HiddenField(
        default=False)
    entrys = serializers.SerializerMethodField()

    class Meta:
        model = EntryInfo
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'user', 'title', 'entrys',
                  'is_delete', 'category')  # 指定序列化的字段

    def get_entrys(self, obj):
        print('obj: ', obj.category.id)
        entrys = Entry.objects.filter(
            category=obj.category)
        entrys_serializer = DicEntrySerializer(entrys, many=True,
                                               context={'request': self.context['request']})
        return entrys_serializer.data


class UserEntrySerializer(serializers.ModelSerializer):

    is_delete = serializers.HiddenField(
        default=False)
    entry_info = serializers.SlugRelatedField(
        slug_field="id", queryset=EntryInfo.objects.all())

    entryship = DicEntrySerializer(many=True, read_only=True)
    entry_Ids = serializers.SlugRelatedField(
        many=True, write_only=True, slug_field="id", queryset=Entry.objects.all())

    # entrys = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Entry.objects.all())

    class Meta:
        model = UserEntry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'name', 'gender', 'height', 'weight', 'age', 'address', 'waistline', 'systolic_pressure', 'diastolic_pressure', 'blood_sugar', 'remark', 'phone', 'entryship',
                  'is_delete',  'entry_Ids', 'entry_info')  # 指定序列化的字段

    def create(self, validated_data):
        entry_Ids = validated_data.pop('entry_Ids')
        userEntry = UserEntry.objects.create(**validated_data)
        for entry_Id in entry_Ids:
            # entry = Entryship.objects.filter(id=entry_Ids)
            UserEntryOfEntry.objects.create(
                user_entry=userEntry, entry=entry_Id)
        return userEntry
