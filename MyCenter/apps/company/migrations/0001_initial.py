# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-28 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('user_name', models.CharField(max_length=16, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='用户密码')),
                ('c_name', models.CharField(max_length=16, verbose_name='企业名称')),
                ('credit_code', models.CharField(max_length=64, verbose_name='信用代码')),
                ('legal_name', models.CharField(max_length=16, verbose_name='法人姓名')),
                ('tel', models.CharField(max_length=11, verbose_name='联系电话')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
                ('site', models.CharField(max_length=64, verbose_name='注册地址')),
                ('province', models.CharField(max_length=32, verbose_name='省')),
                ('city', models.CharField(max_length=32, verbose_name='市')),
                ('c_document', models.ImageField(upload_to='', verbose_name='企业证件')),
                ('c_status', models.SmallIntegerField(choices=[(1, '提交,待审核'), (2, '审核通过'), (3, '审核拒绝')], verbose_name='状态')),
            ],
            options={
                'verbose_name': '用户信息管理',
                'verbose_name_plural': '用户信息管理',
            },
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('type', models.CharField(max_length=20, verbose_name='类型名称')),
            ],
            options={
                'verbose_name': '企业类型',
                'verbose_name_plural': '企业类型',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='c_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyType', verbose_name='企业类型'),
        ),
    ]
