# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150304_0651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datapack',
            old_name='f_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='datapack',
            old_name='l_name',
            new_name='lname',
        ),
    ]
