# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_aboutus_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'static/img/about')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Photograph',
                'verbose_name_plural': 'Photographs',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='staff',
            name='image',
        ),
        migrations.AddField(
            model_name='staff',
            name='photo',
            field=models.ForeignKey(blank=True, to='about.Photo', null=True),
            preserve_default=True,
        ),
    ]
