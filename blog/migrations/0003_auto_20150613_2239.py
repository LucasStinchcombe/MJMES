# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_backgrounds'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Backgrounds',
            new_name='Background',
        ),
    ]
