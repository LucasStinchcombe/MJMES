# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archive',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'static/img/archives', blank=True),
            preserve_default=True,
        ),
    ]
