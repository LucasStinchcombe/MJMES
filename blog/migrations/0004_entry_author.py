# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150222_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.CharField(default='MJMES', max_length=50),
            preserve_default=False,
        ),
    ]
