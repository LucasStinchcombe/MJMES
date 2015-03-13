# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0002_archive_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='thumbnail',
            field=models.ImageField(upload_to=b'static/img/archives'),
        ),
    ]
