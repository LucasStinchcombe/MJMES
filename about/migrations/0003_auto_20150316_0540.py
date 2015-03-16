# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20150316_0523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='photograph',
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='images',
            field=models.ManyToManyField(to=b'about.Photograph', null=True, blank=True),
        ),
    ]
