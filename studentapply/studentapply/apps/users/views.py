from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken

from users import serializers
from users.models import User


class UserAuthorizationView(ObtainJSONWebToken):

    def post(self, request):
        # 调用jwt扩展的方法，对用户登录的数据进行验证
        response = super().post(request)
        serializer = self.get_serializer(data=request.data)
        return response


class PasswordView(GenericAPIView, mixins.UpdateModelMixin):
    """
    用户密码
    """
    queryset = User.objects.all()
    serializer_class = serializers.ResetPasswordSerializer

    def post(self, request, pk):
        return self.update(request, pk)


class UserDetailView(RetrieveAPIView):
    """
    用户详情信息
    /users/<pk>/
    /user/
    """
    serializer_class = serializers.UserDetailSerializer
    # 补充通过认证后才能访问接口的权限
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        返回请求用户对象
        类视图对象中也保存了请求对象request
        request对象的user属性是通过认证插眼后的请求用户对象
        类视图对象还有kwargs属性
        :return: user
        """
        return self.request.user
