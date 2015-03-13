# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20150312_1813'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='Photograph',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='photo',
            new_name='photograph',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='image',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='photograph',
            field=models.ForeignKey(blank=True, to='about.Photograph', null=True),
            preserve_default=True,
        ),
    ]
