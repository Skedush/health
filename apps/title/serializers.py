from rest_framework import serializers
from .models import Title
import time
import datetime


class TitleSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    is_delete = serializers.HiddenField(
        default=False)

    # def validate(self, attrs):
    #     # 调用一个方法生成order_sn
    #     print(attrs)
    #     attrs['is_delete'] = 0
    #     print(attrs)
    #     return attrs

    class Meta:
        model = Title
        # fields = '__all__'  # 序列化全部字段，实际中不建议使用，因为像password等字段是不应该返回给前端的
        fields = ('id','title_name','user','is_delete') # 指定序列化的字段
