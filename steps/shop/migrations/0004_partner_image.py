# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170901_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/partner/<django.db.models.fields.CharField>'),
        ),
    ]