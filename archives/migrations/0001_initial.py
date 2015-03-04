# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.SlugField(max_length=200, unique=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pdf', models.FileField(upload_to=b'static/pdf')),
                ('author', models.CharField(default=b'MJMES', max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('publish', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Archived Edition',
                'verbose_name_plural': 'Archived Editions',
            },
            bases=(models.Model,),
        ),
    ]
