# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_host_os'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dbtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mem', models.CharField(unique=True, max_length=20)),
                ('connections', models.IntegerField()),
                ('iops', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dns', models.URLField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='host',
            name='Region',
            field=models.ForeignKey(default=6, to='main.Region'),
        ),
        migrations.AlterField(
            model_name='host',
            name='os',
            field=models.ForeignKey(default=1, to='main.Os'),
        ),
        migrations.AlterField(
            model_name='region',
            name='regionname',
            field=models.CharField(default=b'cn-hangzhou', max_length=30),
        ),
        migrations.AddField(
            model_name='rds',
            name='Region',
            field=models.ForeignKey(default=6, to='main.Region'),
        ),
        migrations.AddField(
            model_name='rds',
            name='dbtype',
            field=models.ForeignKey(to='main.Dbtype'),
        ),
        migrations.AddField(
            model_name='rds',
            name='group',
            field=models.ForeignKey(to='main.Hostgroup'),
        ),
    ]
