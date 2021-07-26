# Generated by Django 2.2.17 on 2021-07-25 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0005_nation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonContact',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('work_name', models.CharField(max_length=32, verbose_name='工作单位')),
                ('phone', models.CharField(max_length=15, verbose_name='联系电话')),
                ('relation', models.CharField(max_length=15, verbose_name='联系电话')),
            ],
            options={
                'verbose_name': '联系人信息',
                'verbose_name_plural': '联系人信息',
                'db_table': 't_person_contact',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False, verbose_name='id')),
                ('sum_score', models.IntegerField(verbose_name='总分')),
                ('math', models.IntegerField(verbose_name='数学')),
                ('english', models.IntegerField(verbose_name='英语')),
                ('chinese', models.IntegerField(verbose_name='语文')),
                ('physics', models.IntegerField(verbose_name='物理')),
                ('politics', models.IntegerField(verbose_name='政治')),
            ],
            options={
                'verbose_name': '成绩',
                'verbose_name_plural': '成绩',
                'db_table': 't_scores',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='UserApply',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], null=True, verbose_name='性别,1男2女')),
                ('birthday', models.CharField(max_length=32, null=True, verbose_name='生日')),
                ('political_status', models.SmallIntegerField(choices=[(0, '群众'), (1, '团员'), (2, '党员'), (3, '无党派人士')], null=True, verbose_name='政治面貌,1团员2党员')),
                ('is_One_child', models.SmallIntegerField(choices=[(1, '是'), (0, '不是')], null=True, verbose_name='户口,1是0不是')),
                ('residence', models.SmallIntegerField(choices=[(1, '农业户口'), (2, '非农业户口')], null=True, verbose_name='户口,1农业2非农业')),
                ('identity_card', models.CharField(max_length=18, null=True, verbose_name='身份证号')),
                ('police_station', models.CharField(max_length=32, verbose_name='派出所')),
                ('home_address', models.CharField(max_length=56, verbose_name='家庭地址')),
                ('middle_school', models.CharField(max_length=32, verbose_name='中学名称')),
                ('middle_school_class', models.CharField(max_length=10, verbose_name='中学班级')),
                ('teacher', models.CharField(max_length=32, verbose_name='老师')),
                ('teacher_phone', models.CharField(max_length=15, verbose_name='老师联系方式')),
                ('first_wish', models.CharField(max_length=32, verbose_name='第一志愿')),
                ('second_wish', models.CharField(max_length=32, verbose_name='第二志愿')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='city_addresses', to='areas.Area', verbose_name='市')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='district_addresses', to='areas.Area', verbose_name='区')),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='father_UserApply', to='apply.PersonContact', verbose_name='父亲')),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mother_UserApply', to='apply.PersonContact', verbose_name='母亲')),
                ('nation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nation', to='areas.Nation', verbose_name='民族')),
                ('other', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_UserApply', to='apply.PersonContact', verbose_name='其他联系人')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='province_addresses', to='areas.Area', verbose_name='省')),
                ('scores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apply.Scores', verbose_name='scoreId')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='UserId')),
            ],
            options={
                'verbose_name': '报名信息',
                'verbose_name_plural': '报名信息',
                'db_table': 't_user_apply',
                'ordering': ('id',),
            },
        ),
    ]
