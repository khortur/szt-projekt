# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-22 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_purchase_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='amount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
