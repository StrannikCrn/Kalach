# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-20 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='workType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.WorkType', verbose_name='Тип работ'),
        ),
        migrations.AlterField(
            model_name='work',
            name='name',
            field=models.CharField(default=0, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='work',
            name='text',
            field=models.CharField(default=0, max_length=1000, verbose_name='Текси'),
        ),
        migrations.AlterField(
            model_name='worktype',
            name='name',
            field=models.CharField(default=0, max_length=200, verbose_name='Название'),
        ),
    ]
