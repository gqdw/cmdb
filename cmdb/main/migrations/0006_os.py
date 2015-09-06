# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150905_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Os',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('osname', models.CharField(default=b'Centos6', max_length=10, blank=True)),
            ],
        ),
    ]
