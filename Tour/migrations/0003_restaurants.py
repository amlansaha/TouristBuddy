# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0002_spots'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('restaurant_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('restaurant_name', models.CharField(max_length=50)),
                ('restaurant_website', models.CharField(null=True, max_length=50, blank=True)),
                ('restaurant_phone', models.CharField(null=True, max_length=20, blank=True)),
                ('restaurant_email', models.CharField(null=True, max_length=20, blank=True)),
                ('location', models.ForeignKey(to='Tour.Locations')),
            ],
            options={
                'managed': True,
                'db_table': 'restaurants',
            },
        ),
    ]
