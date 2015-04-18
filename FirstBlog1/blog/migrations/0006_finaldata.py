# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150304_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='finalData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('fname', models.CharField(max_length=32)),
                ('lname', models.CharField(max_length=64)),
                ('mname', models.CharField(max_length=32)),
                ('DOB', models.CharField(max_length=16)),
                ('BirthP', models.CharField(max_length=64)),
                ('gender', models.CharField(max_length=32)),
                ('genderHide', models.CharField(max_length=32)),
                ('SOC', models.CharField(max_length=32)),
                ('mAddress', models.CharField(max_length=64)),
                ('mAddress2', models.CharField(max_length=64)),
                ('mAddressCity', models.CharField(max_length=64)),
                ('mAddressState', models.CharField(max_length=64)),
                ('sAddress', models.CharField(max_length=64)),
                ('sAddress2', models.CharField(max_length=64)),
                ('sAddressCity', models.CharField(max_length=64)),
                ('sAddressState', models.CharField(max_length=64)),
                ('hPhone', models.CharField(max_length=16)),
                ('unlisted', models.BooleanField()),
                ('Father', models.BooleanField()),
                ('Mother', models.BooleanField()),
                ('Guardian', models.BooleanField()),
                ('FatherName', models.CharField(max_length=32)),
                ('FatherWNum', models.CharField(max_length=32)),
                ('FatherCNum', models.CharField(max_length=32)),
                ('MotherName', models.CharField(max_length=32)),
                ('MotherWNum', models.CharField(max_length=32)),
                ('MotherCNum', models.CharField(max_length=32)),
                ('school', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
