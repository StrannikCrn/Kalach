# Generated by Django 2.0.7 on 2018-08-10 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180810_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
    ]
