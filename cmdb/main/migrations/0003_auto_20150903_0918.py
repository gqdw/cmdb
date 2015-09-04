# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150903_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='beizhu',
            field=models.TextField(blank=True),
        ),
    ]
