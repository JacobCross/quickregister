# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_squashed_0014_auto_20150327_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finaldata',
            name='father',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='finaldata',
            name='gender',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='finaldata',
            name='genderhide',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='finaldata',
            name='guardian',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='finaldata',
            name='mother',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='finaldata',
            name='unlisted',
            field=models.BooleanField(),
        ),
    ]
