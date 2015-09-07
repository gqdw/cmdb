# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150907_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbtype',
            name='connections',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dbtype',
            name='iops',
            field=models.IntegerField(),
        ),
    ]
