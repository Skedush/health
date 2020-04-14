from rest_framework import serializers
from .models import EntryInfo, UserEntry, UserEntryOfEntry
from dicEntry.models import Entry, Entryship
from category.models import Category
from dicEntry.serializers import DicEntrySerializer, EntrySerializer
from category.serializers import ResultCategorySerializer
from title.serializers import TitleSerializer


class UserEntryDicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ( 'title')  # 指定序列化的字段


class EntryInfoSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    is_delete = serializers.HiddenField(
        default=False)
    entrys = serializers.SerializerMethodField()
    # title=TitleSerializer()

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

    # entryship = UserEntryDicSerializer(many=True, read_only=True)
    # entryship = serializers.SlugRelatedField(
    #     many=True, read_only=True, slug_field="title")
    entry_Ids = serializers.SlugRelatedField(
        many=True, write_only=True, slug_field="id", queryset=Entry.objects.all())
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    # entrys = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Entry.objects.all())

    class Meta:
        model = UserEntry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        # fields = ('id', 'name', 'gender', 'height', 'weight', 'age', 'address', 'waistline', 'systolic_pressure', 'diastolic_pressure', 'blood_sugar', 'remark', 'phone', 'entryship',
        #           'is_delete',  'entry_Ids', 'entry_info')  # 指定序列化的字段
        fields = ('id', 'name', 'gender', 'height', 'weight', 'age', 'address', 'waistline', 'systolic_pressure', 'diastolic_pressure', 'blood_sugar', 'remark', 'phone' ,'created',
                    'is_delete',  'entry_Ids', 'entry_info')  # 指定序列化的字段

    def create(self, validated_data):
        entry_Ids = validated_data.pop('entry_Ids')
        userEntry = UserEntry.objects.create(**validated_data)
        for entry_Id in entry_Ids:
            # entry = Entryship.objects.filter(id=entry_Ids)
            UserEntryOfEntry.objects.create(
                user_entry=userEntry, entry=entry_Id)
        return userEntry


class ResultUserEntrySerializer(serializers.ModelSerializer):
    entry_info = serializers.SlugRelatedField(
        slug_field="id", queryset=EntryInfo.objects.all())

    entryship = EntrySerializer(many=True, read_only=True)

    # result = serializers.SerializerMethodField(label='结果展示')

    # entrys = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Entry.objects.all())

    class Meta:
        model = UserEntry
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id', 'name', 'gender', 'height', 'weight', 'age', 'address', 'waistline', 'systolic_pressure', 'diastolic_pressure', 'blood_sugar', 'remark', 'phone', 'entryship',
                  'entry_info')  # 指定序列化的字段

    # def get_result(self, obj):
    #     """
    #     返回当前角色用户数量
    #     固定写法,obj代表Role实例对象,模型类配置了反向引用user代表当前角色用户
    #     """
    #     entryShip = obj.entryship.all()

    #     # categorys = Category.objects.exclude(
    #     #     id=obj.entry_info.category.id)
    #     categorys = Category.objects.filter(
    #         entrys__title='肾')

    #     for categoryInfo in categorys:
    #         temp = []
    #         for entrySelect in entryShip:
    #             entrys = Entryship.objects.filter(
    #                 from_entry=entrySelect, category=categoryInfo)
    #             for entry in entrys:
    #                 entry.to_entry.category
    #                 # print(entry.to_entry.category)
    #                 temp.append(entry.to_entry)

    #     # categoryInfo.entrys.set(temp)

    #     return ResultCategorySerializer(categorys, many=True, read_only=True).data
