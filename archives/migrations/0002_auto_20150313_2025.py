# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'static/img/archives')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='archive',
            options={'ordering': ['created'], 'verbose_name': 'Archived Edition', 'verbose_name_plural': 'Archived Editions'},
        ),
        migrations.AddField(
            model_name='archive',
            name='thumbnail',
            field=models.ForeignKey(blank=True, to='archives.Thumbnail', null=True),
            preserve_default=True,
        ),
    ]
