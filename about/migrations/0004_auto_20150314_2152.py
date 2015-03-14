# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20150314_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photograph',
            name='image',
            field=models.ImageField(upload_to=b'about/static/img'),
        ),
    ]
