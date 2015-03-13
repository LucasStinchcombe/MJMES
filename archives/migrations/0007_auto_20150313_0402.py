# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0006_auto_20150312_2328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archive',
            options={'ordering': ['created'], 'verbose_name': 'Archived Edition', 'verbose_name_plural': 'Archived Editions'},
        ),
    ]
