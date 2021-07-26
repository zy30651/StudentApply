from django.shortcuts import render

# Create your views here.
from .serializers import LogSerializer
from .models import Logs
from studentapply.utils.CustomModelViewSet import CustomModelViewSet


class LogsViewSet(CustomModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogSerializer

    def destroy(self, request, *args, **kwargs):
        pass
