# Generated by Django 2.2.17 on 2021-07-25 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0003_auto_20210725_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='area',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subs', to='areas.Area', verbose_name='上级行政区划'),
        ),
        migrations.AlterField(
            model_name='area',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]