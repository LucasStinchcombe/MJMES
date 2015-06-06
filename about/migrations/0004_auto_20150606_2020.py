# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150606_2020'),
        ('about', '0003_auto_20150316_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='photograph',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
