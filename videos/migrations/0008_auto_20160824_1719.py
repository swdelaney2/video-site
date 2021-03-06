# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20160824_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='videos/static/images'),
        ),
    ]
