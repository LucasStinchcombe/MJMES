# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150613_2239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='background',
            options={'ordering': ['app']},
        ),
        migrations.AddField(
            model_name='background',
            name='app',
            field=models.CharField(default=b'NO', max_length=2, choices=[(b'AB', b'About'), (b'AR', b'Archives'), (b'BL', b'Blog'), (b'CO', b'Contact'), (b'NO', b'None')]),
            preserve_default=True,
        ),
    ]
