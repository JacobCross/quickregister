# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150327_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='finaldata',
            name='unlisted',
            field=models.BooleanField(default='absent'),
            preserve_default=False,
        ),
    ]
