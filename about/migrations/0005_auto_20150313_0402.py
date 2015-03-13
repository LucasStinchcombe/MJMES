# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20150312_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='images',
            field=models.ManyToManyField(related_name=b'additional image', null=True, to='about.Photograph', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='photograph',
            field=models.ForeignKey(related_name=b'main photograph', blank=True, to='about.Photograph', null=True),
        ),
    ]
