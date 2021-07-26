from rest_framework import serializers
from .models import Area, Nation


class AreaSerializer(serializers.ModelSerializer):
    """行政区域信息序列化器"""
    class Meta:
        model = Area
        fields = ('id', 'name')


class SubAreaSerializer(serializers.ModelSerializer):
    """子集的区域信息序列化器"""
    subs = AreaSerializer(many=True, read_only=True)

    class Meta:
        model = Area
        fields = ('id', 'name', 'subs')  # 对应related_name的设置


class NationSerializer(serializers.ModelSerializer):
    """民族序列化器"""
    class Meta:
        model = Nation
        fields = ('id', 'name')
