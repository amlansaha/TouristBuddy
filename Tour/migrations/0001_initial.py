# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjacent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('distance_in_km', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'adjacent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('district_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('district_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'districts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Guides',
            fields=[
                ('guide_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('guide_name', models.CharField(max_length=80)),
                ('contact_no', models.CharField(max_length=20)),
                ('guide_email', models.CharField(null=True, blank=True, max_length=50)),
            ],
            options={
                'db_table': 'guides',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('hotel_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_website', models.CharField(null=True, blank=True, max_length=50)),
                ('hotel_phone', models.CharField(null=True, blank=True, max_length=20)),
                ('hotel_email', models.CharField(null=True, blank=True, max_length=20)),
            ],
            options={
                'db_table': 'hotels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('image_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('image_dir', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('location_name', models.CharField(max_length=50)),
                ('description', models.CharField(null=True, blank=True, max_length=300)),
                ('map', models.CharField(null=True, blank=True, max_length=20)),
            ],
            options={
                'db_table': 'locations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('charge', models.FloatField()),
            ],
            options={
                'db_table': 'manage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('location_id', models.CharField(max_length=20)),
                ('review', models.CharField(null=True, blank=True, max_length=300)),
                ('rating', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('travel_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('transport_type', models.CharField(max_length=20)),
                ('transport_name', models.CharField(null=True, blank=True, max_length=40)),
                ('contact_email', models.CharField(null=True, blank=True, max_length=50)),
                ('contact_website', models.CharField(null=True, blank=True, max_length=30)),
                ('contact_phone', models.CharField(null=True, blank=True, max_length=20)),
            ],
            options={
                'db_table': 'travel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('user_email', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
