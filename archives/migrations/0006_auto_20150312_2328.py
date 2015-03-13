# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0005_auto_20150312_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='image',
            field=models.ImageField(upload_to=b'static/img/archives'),
        ),
    ]
