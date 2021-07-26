from django.db import models
from users.models import User

residence = (
    (1, '农业户口'),
    (2, '非农业户口')
)
# 中共党员、共青团员、民革党员、民盟盟员、无党派人士、群众等,要根据
political = (
    (0, '群众'),
    (1, '团员'),
    (2, '党员'),
    (3, '无党派人士')
)
is_One_child = (
    (1, '是'),
    (0, '不是')
)
gender = (
    (1, '男'),
    (2, '女')
)


class PersonContact(models.Model):
    """
    联系人信息
    """
    id = models.CharField(max_length=24, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=32, verbose_name='名称')
    work_name = models.CharField(max_length=32, verbose_name='工作单位')
    phone = models.CharField(max_length=15, verbose_name='联系电话')
    relation = models.CharField(max_length=15, verbose_name='联系电话')

    class Meta:
        db_table = 't_person_contact'
        verbose_name = '联系人信息'
        verbose_name_plural = '联系人信息'
        ordering = ('id',)


class Scores(models.Model):
    """
    成绩
    """
    id = models.CharField(max_length=24, primary_key=True, verbose_name='id')
    sum_score = models.IntegerField(verbose_name='总分')
    math = models.IntegerField(verbose_name='数学')
    english = models.IntegerField(verbose_name='英语')
    chinese = models.IntegerField(verbose_name='语文')
    physics = models.IntegerField(verbose_name='物理')
    politics = models.IntegerField(verbose_name='政治')
    chemistry = models.IntegerField(verbose_name='化学')
    history = models.IntegerField(verbose_name='历史')
    sports = models.IntegerField(verbose_name='体育')
    other = models.IntegerField(verbose_name='额外加分')

    class Meta:
        db_table = 't_scores'
        verbose_name = '成绩'
        verbose_name_plural = '成绩'
        ordering = ('id',)


class UserApply(models.Model):
    """
    报名信息
    """
    id = models.CharField(max_length=24, primary_key=True, verbose_name='id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='UserId')
    name = models.CharField(null=True, max_length=32, verbose_name='姓名')
    gender = models.SmallIntegerField(null=True, choices=gender, verbose_name='性别,1男2女')
    birthday = models.CharField(null=True, max_length=32, verbose_name='生日')
    nation = models.ForeignKey('areas.Nation', on_delete=models.PROTECT, related_name='nation', verbose_name='民族')
    political_status = models.SmallIntegerField(null=True, choices=political, verbose_name='政治面貌,1团员2党员')
    is_One_child = models.SmallIntegerField(null=True, choices=is_One_child, verbose_name='户口,1是0不是')
    residence = models.SmallIntegerField(null=True, choices=residence, verbose_name='户口,1农业2非农业')

    identity_card = models.CharField(null=True, max_length=18, verbose_name='身份证号')
    province = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='province_addresses', verbose_name='省')
    city = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='city_addresses', verbose_name='市')
    district = models.ForeignKey('areas.Area', on_delete=models.PROTECT, related_name='district_addresses', verbose_name='区')
    police_station = models.CharField(max_length=32, verbose_name='派出所')

    home_address = models.CharField(max_length=56, verbose_name='家庭地址')
    middle_school = models.CharField(max_length=32, verbose_name='中学名称')
    middle_school_class = models.CharField(max_length=10, verbose_name='中学班级')
    teacher = models.CharField(max_length=32, verbose_name='老师')
    teacher_phone = models.CharField(max_length=15, verbose_name='老师联系方式')
    first_wish = models.CharField(max_length=32, verbose_name='第一志愿')
    second_wish = models.CharField(max_length=32, verbose_name='第二志愿')

    father = models.ForeignKey(PersonContact, on_delete=models.CASCADE, related_name='father_UserApply', verbose_name='父亲')
    mother = models.ForeignKey(PersonContact, on_delete=models.CASCADE, related_name='mother_UserApply', verbose_name='母亲')
    other = models.ForeignKey(PersonContact, on_delete=models.CASCADE, related_name='other_UserApply', verbose_name='其他联系人')

    scores = models.ForeignKey(Scores, on_delete=models.CASCADE, verbose_name='scoreId')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 't_user_apply'
        verbose_name = '报名信息'
        verbose_name_plural = '报名信息'
        ordering = ('id',)


