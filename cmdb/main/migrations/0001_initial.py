# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=30)),
                ('eth0', models.GenericIPAddressField()),
                ('eth1', models.GenericIPAddressField()),
                ('beizhu', models.TextField()),
                ('Region', models.CharField(max_length=3, choices=[(b'hz', b'cn-hangzhou'), (b'ss', b'cn-shenzhen'), (b'qd', b'cn-qingdao'), (b'bj', b'cn-beijing'), (b'sh', b'cn-shanghai'), (b'hk', b'cn-hongkong'), (b'us1', b'us-west-1')])),
                ('test', models.TextField()),
                ('test2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hostgroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='group',
            field=models.ForeignKey(to='main.Hostgroup'),
        ),
    ]
