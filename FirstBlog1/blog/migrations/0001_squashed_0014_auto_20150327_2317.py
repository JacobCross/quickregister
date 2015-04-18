# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    replaces = [(b'blog', '0001_initial'), (b'blog', '0002_dataform'), (b'blog', '0003_auto_20150228_1806'), (b'blog', '0004_auto_20150304_0651'), (b'blog', '0005_auto_20150304_0712'), (b'blog', '0006_finaldata'), (b'blog', '0007_remove_finaldata_date'), (b'blog', '0008_remove_finaldata_genderhide'), (b'blog', '0009_remove_finaldata_gender'), (b'blog', '0010_auto_20150327_2011'), (b'blog', '0011_auto_20150327_2117'), (b'blog', '0012_auto_20150327_2138'), (b'blog', '0013_finaldata_unlisted'), (b'blog', '0014_auto_20150327_2317')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('bodytext', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='datapack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='finalData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=32)),
                ('lname', models.CharField(max_length=64)),
                ('mname', models.CharField(max_length=32)),
                ('dob', models.CharField(max_length=16)),
                ('birthp', models.CharField(max_length=64)),
                ('soc', models.CharField(max_length=32)),
                ('maddress', models.CharField(max_length=64)),
                ('maddress2', models.CharField(max_length=64)),
                ('maddresscity', models.CharField(max_length=64)),
                ('maddressstate', models.CharField(max_length=64)),
                ('saddress', models.CharField(max_length=64)),
                ('saddress2', models.CharField(max_length=64)),
                ('saddresscity', models.CharField(max_length=64)),
                ('saddressstate', models.CharField(max_length=64)),
                ('hphone', models.CharField(max_length=16)),
                ('fathername', models.CharField(max_length=32)),
                ('fatherwnum', models.CharField(max_length=32)),
                ('fathercnum', models.CharField(max_length=32)),
                ('mothername', models.CharField(max_length=32)),
                ('motherwnum', models.CharField(max_length=32)),
                ('mothercnum', models.CharField(max_length=32)),
                ('school', models.CharField(max_length=128)),
                ('gender', models.CharField(default=datetime.date(2015, 3, 27), max_length=32)),
                ('genderhide', models.CharField(default=datetime.date(2015, 3, 27), max_length=32)),
                ('unlisted', models.BooleanField(default='absent')),
                ('father', models.BooleanField(default='0')),
                ('guardian', models.BooleanField(default='0')),
                ('mother', models.BooleanField(default='0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
