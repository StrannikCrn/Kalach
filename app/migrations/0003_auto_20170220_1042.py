# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-20 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170220_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='Дата окончания проекта'),
        ),
        migrations.AlterField(
            model_name='work',
            name='text',
            field=models.CharField(default=0, max_length=1000, verbose_name='Текст'),
        ),
    ]
