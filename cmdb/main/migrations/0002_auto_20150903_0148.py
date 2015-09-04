# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('regionname', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='host',
            name='test',
        ),
        migrations.RemoveField(
            model_name='host',
            name='test2',
        ),
        migrations.AlterField(
            model_name='host',
            name='Region',
            field=models.ForeignKey(to='main.Region'),
        ),
    ]
