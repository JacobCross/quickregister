# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150327_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='finaldata',
            name='gender',
            field=models.CharField(default=datetime.date(2015, 3, 27), max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finaldata',
            name='genderhide',
            field=models.CharField(default=datetime.date(2015, 3, 27), max_length=32),
            preserve_default=False,
        ),
    ]
