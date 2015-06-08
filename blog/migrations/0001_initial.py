# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('id', models.SlugField(max_length=200, unique=True, serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Blog Entry',
                'verbose_name_plural': 'Blog Entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'blog/img')),
                ('caption', models.TextField(null=True, blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region', models.CharField(unique=True, max_length=200)),
                ('id', models.SlugField(max_length=200, unique=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag', models.CharField(max_length=200)),
                ('id', models.SlugField(max_length=200, unique=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='entry',
            name='images',
            field=models.ManyToManyField(related_name=b'figures and tables', to='blog.Image', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='photograph',
            field=models.ForeignKey(related_name=b'main photograph', to='blog.Image', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='region',
            field=models.ManyToManyField(to='blog.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
            preserve_default=True,
        ),
    ]
