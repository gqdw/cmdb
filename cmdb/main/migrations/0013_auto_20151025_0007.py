# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150907_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='os',
            name='osname',
            field=models.CharField(default=b'Centos6', unique=True, max_length=10, blank=True),
        ),
    ]
