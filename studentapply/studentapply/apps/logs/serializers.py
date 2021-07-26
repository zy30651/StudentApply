from rest_framework import serializers
from .models import Logs
import bson


class LogSerializer(serializers.ModelSerializer):
    """
    日志信息序列化器
    """

    class Meta:
        model = Logs
        fields = ('id', 'user', 'action', 'desc', 'action_time', 'create_time')
        read_only_fields = ('id', 'create_time')

    def create(self, validated_data):
        validated_data['id'] = bson.ObjectId()
        return Logs.objects.create(**validated_data)
