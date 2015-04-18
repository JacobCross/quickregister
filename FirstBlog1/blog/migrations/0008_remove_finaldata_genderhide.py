# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_finaldata_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finaldata',
            name='genderHide',
        ),
    ]
