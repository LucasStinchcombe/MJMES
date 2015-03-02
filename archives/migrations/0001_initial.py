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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pdf', models.FileField(upload_to=b'/static/pdf')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('publish', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Archive Entry',
                'verbose_name_plural': 'Archive Entries',
            },
            bases=(models.Model,),
        ),
    ]
