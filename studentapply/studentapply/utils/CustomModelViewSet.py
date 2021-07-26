import json
from rest_framework import viewsets
from rest_framework.response import Response
import logging
logger = logging.getLogger('django.request')


class ReturnMsg:
    def __init__(self, code=200, msg='成功', errors=None, data=None):
        self.code = code
        self.msg = msg
        self.errors = {} if errors is None else errors
        self.data = [] if data is None else data

    def dict(self):
        return {
            'code': self.code,
            'msg': self.msg,
            'errors': self.errors,
            'data': self.data
        }


class CustomModelViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        logger.debug('create')
        response = super().create(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    def retrieve(self, request, *args, **kwargs):
        logger.debug('retrieve')
        response = super().retrieve(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    def update(self, request, *args, **kwargs):
        logger.debug('update')
        response = super().update(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    def destroy(self, request, *args, **kwargs):
        logger.debug('destroy')
        serializer = self.get_serializer(self.get_object())
        response = Response(serializer.data)
        super().destroy(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    # def list(self, request, *args, **kwargs):
    #     response = super().list(request, *args, **kwargs)
    #     return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    def list(self, request, *args, **kwargs):
        logger.debug('list')
        search_key = self.request.query_params.get('searchKey')
        queryset = self.filter_queryset(self.get_queryset())
        if search_key is not None:
            queryset = queryset.filter(name__contains=search_key)

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

        serializer = self.get_serializer(queryset, many=True)
        response = Response(serializer.data)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)
