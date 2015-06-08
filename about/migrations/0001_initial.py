# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'test', max_length=200)),
                ('content', models.TextField()),
                ('publish', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('modified', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'about/img')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Photograph',
                'verbose_name_plural': 'Photographs',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='images',
            field=models.ManyToManyField(to='about.Photograph', null=True, blank=True),
            preserve_default=True,
        ),
    ]
