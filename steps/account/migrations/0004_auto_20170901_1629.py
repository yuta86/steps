# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170831_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='social_status',
            field=models.CharField(choices=[('Школьник', 'schoolboy'), ('Студент', 'student'), ('Рабочий', 'working'), ('Госслужащий', 'сivil_servant'), ('Предприниматель', 'businessman'), ('Безработный', 'unemployed'), ('Другое', 'other')], default='other', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('Заблокирован', 'blocked'), ('Активный', 'activated'), ('Ожидает активацию', 'waits for activation')], default='waits for activation', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('мужской', 'male'), ('женский', 'female')], default='male', max_length=10),
        ),
    ]
