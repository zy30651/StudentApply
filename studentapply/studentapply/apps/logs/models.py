from django.db import models
from users.models import User


# Create your models here.
class Logs(models.Model):
    """
    日志
    """
    id = models.CharField(max_length=24, primary_key=True, verbose_name='id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='UserId')
    action = models.CharField(max_length=32, verbose_name='操作')
    desc = models.CharField(max_length=255, verbose_name='操作详情')
    action_time = models.BigIntegerField(verbose_name='发生时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='日志创建时间')

    class Meta:
        db_table = 't_logs'
        verbose_name = '日志记录'
        verbose_name_plural = '日志记录'
        ordering = ('id',)
