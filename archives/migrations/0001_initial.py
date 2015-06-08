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
                ('title', models.CharField(max_length=200)),
                ('pdf', models.FileField(upload_to=b'archives/pdf')),
                ('author', models.CharField(default=b'MJMES', max_length=200)),
                ('created', models.DateField()),
                ('modified', models.DateField(auto_now=True)),
                ('publish', models.BooleanField(default=True)),
                ('id', models.SlugField(max_length=200, unique=True, serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'Archived Edition',
                'verbose_name_plural': 'Archived Editions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'archives/thumbnails')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='archive',
            name='thumbnail',
            field=models.ForeignKey(blank=True, to='archives.Thumbnail', null=True),
            preserve_default=True,
        ),
    ]
