# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150304_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='id',
            field=models.SlugField(max_length=200, unique=True, serialize=False, primary_key=True),
        ),
    ]
