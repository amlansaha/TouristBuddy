# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesGuide',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=20)),
            ],
            options={
                'db_table': 'images_guide',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImagesLocation',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=20)),
            ],
            options={
                'db_table': 'images_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImagesUser',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=20)),
            ],
            options={
                'db_table': 'images_user',
                'managed': False,
            },
        ),
    ]
