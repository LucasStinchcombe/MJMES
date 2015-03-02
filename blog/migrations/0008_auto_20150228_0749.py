# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
