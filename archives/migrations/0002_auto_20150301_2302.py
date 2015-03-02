# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archive',
            options={'ordering': ['-created'], 'verbose_name': 'Archived Edition', 'verbose_name_plural': 'Archived Editions'},
        ),
        migrations.AddField(
            model_name='archive',
            name='author',
            field=models.CharField(default=b'MJMES', max_length=200),
            preserve_default=True,
        ),
    ]
