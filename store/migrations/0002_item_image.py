# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-22 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
