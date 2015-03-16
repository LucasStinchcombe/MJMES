# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0002_auto_20150316_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='created',
            field=models.DateField(),
        ),
    ]
