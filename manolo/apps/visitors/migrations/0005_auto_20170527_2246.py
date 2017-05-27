# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0004_auto_20170325_0254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('number_of_visits', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='number_of_visits',
        ),
        migrations.AddField(
            model_name='statistic',
            name='data',
            field=models.TextField(null=True),
        ),
    ]