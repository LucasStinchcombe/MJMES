# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0003_auto_20150301_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archive',
            name='id',
        ),
        migrations.AlterField(
            model_name='archive',
            name='title',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
    ]
