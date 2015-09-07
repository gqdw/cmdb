# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150907_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rds',
            name='dns',
            field=models.CharField(max_length=50),
        ),
    ]
