# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spots',
            fields=[
                ('spot_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('spot_name', models.CharField(max_length=50)),
                ('location', models.ForeignKey(to='Tour.Locations', related_name='tour_spots_location')),
            ],
            options={
                'managed': True,
                'db_table': 'spots',
            },
        ),
    ]
