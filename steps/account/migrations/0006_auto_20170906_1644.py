# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20170904_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30, verbose_name='Населённый пункт'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%Y-%m-%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('male', 'мужской'), ('female', 'женский')], default='male', max_length=10, verbose_name='пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_status',
            field=models.CharField(choices=[('schoolboy', 'Школьник'), ('student', 'Студент'), ('working', 'Рабочий'), ('сivil_servant', 'Госслужащий'), ('businessman', 'Предприниматель'), ('unemployed', 'Безработный'), ('other', 'Другое')], default='other', max_length=20, verbose_name='Социальный статус'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('blocked', 'Заблокирован'), ('activated', 'Активный'), ('waits for activation', 'Ожидает активацию')], default='waits for activation', max_length=50, verbose_name='Статус'),
        ),
    ]
