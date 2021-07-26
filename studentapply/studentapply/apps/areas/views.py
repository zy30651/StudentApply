from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Area, Nation
from . import serializers


class AreasViewSet(ReadOnlyModelViewSet):
    """
    list:返回所有省份的信息
    retrieve：返回特定省或市的下属行政区
    """
    pagination_class = None  # 区划信息不分页

    def get_queryset(self):
        if self.action == 'list':
            return Area.objects.filter(parent=None)
        else:
            return Area.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.AreaSerializer
        else:
            return serializers.SubAreaSerializer


class NationViewSet(ReadOnlyModelViewSet):
    """
    list:返回所有民族的信息
    """
    pagination_class = None  # 区划信息不分页
    queryset = Nation.objects.all()
    serializer_class = serializers.NationSerializer
    
