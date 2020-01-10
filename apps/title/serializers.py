from rest_framework import serializers
from .models import Title
import time
import datetime


class TitleSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     title = super(TitleSerializer, self).create(
    #         validated_data=validated_data)
    #     title.set_user()
    #     title.save()
    #     return title

    class Meta:
        model = Title
        fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        # fields = ('id','username','phone','email') # 指定序列化的字段
