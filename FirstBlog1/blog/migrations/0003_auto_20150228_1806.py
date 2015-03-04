# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_dataform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataform',
            old_name='fname',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='dataform',
            old_name='lname',
            new_name='l_name',
        ),
    ]
