# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_entry_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='subtitle',
            field=models.CharField(default='This is the sub-title', max_length=200),
            preserve_default=False,
        ),
    ]
