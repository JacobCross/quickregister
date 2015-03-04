# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150228_1806'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dataform',
            new_name='datapack',
        ),
    ]
