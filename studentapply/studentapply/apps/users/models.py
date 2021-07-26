from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from itsdangerous import TimedJSONWebSignatureSerializer as TJWSSerializer, BadData
from django.conf import settings


# Create your models here.
class User(AbstractUser):

    class Meta:
        db_table = "tb_users"
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def generate_set_password_token(self):
        """
        生成修改密码的token
        """
        serializer = TJWSSerializer(settings.SECRET_KEY, expires_in=300)
        data = {'user_id': self.id}
        token = serializer.dumps(data)
        return token.decode()

    @staticmethod
    def check_set_password_token(token, user_id):
        """
        检验设置密码的token
        """
        serializer = TJWSSerializer(settings.SECRET_KEY, expires_in=300)
        try:
            data = serializer.loads(token)
        except BadData:
            return False
        else:
            if user_id != str(data.get('user_id')):
                return False
            else:
                return True


admin.site.register(User)
