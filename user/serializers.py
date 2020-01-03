from rest_framework import serializers
from .models import User
import time
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        # fields = ('id','username','phone','email') # 指定序列化的字段
