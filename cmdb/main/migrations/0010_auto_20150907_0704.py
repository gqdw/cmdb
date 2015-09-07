# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150907_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbtype',
            name='mem',
            field=models.IntegerField(unique=True),
        ),
    ]
