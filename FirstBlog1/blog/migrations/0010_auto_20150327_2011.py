# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_finaldata_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finaldata',
            name='Father',
        ),
        migrations.RemoveField(
            model_name='finaldata',
            name='Guardian',
        ),
        migrations.RemoveField(
            model_name='finaldata',
            name='Mother',
        ),
        migrations.RemoveField(
            model_name='finaldata',
            name='unlisted',
        ),
    ]
