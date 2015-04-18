# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_finaldata_unlisted'),
    ]

    operations = [
        migrations.AddField(
            model_name='finaldata',
            name='father',
            field=models.BooleanField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finaldata',
            name='guardian',
            field=models.BooleanField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finaldata',
            name='mother',
            field=models.BooleanField(default='0'),
            preserve_default=False,
        ),
    ]
