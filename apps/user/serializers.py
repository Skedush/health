from rest_framework import serializers
from .models import User
from title.models import Title
from userEntry.models import EntryInfo
from category.models import Category


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        print(validated_data)
        titleName = validated_data.pop('title')
        user = super(UserSerializer, self).create(
            validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        title = Title(title_name=titleName, user=user)
        title.save()
        category = Category.objects.get(name='320症状')
        entryInfo = EntryInfo(category=category, title=title, user=user)
        entryInfo.save()
        return user

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance=instance,
                                                  validated_data=validated_data)
        user.set_password(validated_data['password'])

        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        # fields = ('id', 'username', 'phone', 'email', 'title')  # 指定序列化的字段
