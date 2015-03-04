# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='id',
            field=models.SlugField(primary_key=True, serialize=False, editable=False, max_length=200, unique=True),
        ),
    ]
