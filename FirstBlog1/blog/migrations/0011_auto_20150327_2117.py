# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150327_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finaldata',
            old_name='BirthP',
            new_name='birthp',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='DOB',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='FatherCNum',
            new_name='fathercnum',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='FatherName',
            new_name='fathername',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='FatherWNum',
            new_name='fatherwnum',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='hPhone',
            new_name='hphone',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='mAddress',
            new_name='maddress',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='mAddress2',
            new_name='maddress2',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='mAddressCity',
            new_name='maddresscity',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='mAddressState',
            new_name='maddressstate',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='MotherCNum',
            new_name='mothercnum',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='MotherName',
            new_name='mothername',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='MotherWNum',
            new_name='motherwnum',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='sAddress',
            new_name='saddress',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='sAddress2',
            new_name='saddress2',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='sAddressCity',
            new_name='saddresscity',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='sAddressState',
            new_name='saddressstate',
        ),
        migrations.RenameField(
            model_name='finaldata',
            old_name='SOC',
            new_name='soc',
        ),
    ]
