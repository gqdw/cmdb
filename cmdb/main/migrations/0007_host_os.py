# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_os'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='os',
            field=models.ForeignKey(default=1, to='main.Os'),
            preserve_default=False,
        ),
    ]
