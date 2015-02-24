# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ForeignKey(default=1, to='blog.Image'),
            preserve_default=True,
        ),
    ]
