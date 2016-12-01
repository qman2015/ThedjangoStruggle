# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_theater'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_basic_type', models.CharField(blank=True, default='', max_length=100)),
                ('subgenre_type', models.CharField(blank=True, default='', max_length=100)),
                ('genre_classification', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('genre_classification',),
            },
        ),
    ]