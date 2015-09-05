# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='eth0',
            field=models.GenericIPAddressField(unique=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='eth1',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
