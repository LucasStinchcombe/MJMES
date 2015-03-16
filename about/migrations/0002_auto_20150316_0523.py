# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='staff',
            name='image',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='images',
            field=models.ManyToManyField(related_name=b'additional images', null=True, to='about.Photograph', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='photograph',
            field=models.ForeignKey(related_name=b'main photograph', blank=True, to='about.Photograph', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staff',
            name='photograph',
            field=models.ForeignKey(blank=True, to='about.Photograph', null=True),
            preserve_default=True,
        ),
    ]
