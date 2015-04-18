# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_finaldata_genderhide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finaldata',
            name='gender',
        ),
    ]
