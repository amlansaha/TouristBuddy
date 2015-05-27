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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('distance_in_km', models.FloatField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'adjacent',
            },
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('dist_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('dist_name', models.CharField(max_length=20)),
            ],
            options={
                'managed': True,
                'db_table': 'districts',
            },
        ),
        migrations.CreateModel(
            name='Guides',
            fields=[
                ('guide_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('guide_name', models.CharField(max_length=80)),
                ('contact_no', models.CharField(max_length=20)),
                ('guide_email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'guides',
            },
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('hotel_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_website', models.CharField(blank=True, max_length=50, null=True)),
                ('hotel_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('hotel_email', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'hotels',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('image_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('image_dir', models.CharField(max_length=40)),
            ],
            options={
                'managed': True,
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='ImagesGuide',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('guide', models.ForeignKey(to='Tour.Guides')),
                ('image', models.ForeignKey(to='Tour.Images')),
            ],
            options={
                'managed': True,
                'db_table': 'images_guide',
            },
        ),
        migrations.CreateModel(
            name='ImagesLocation',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('image', models.ForeignKey(to='Tour.Images')),
            ],
            options={
                'managed': True,
                'db_table': 'images_location',
            },
        ),
        migrations.CreateModel(
            name='ImagesUser',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('image', models.ForeignKey(to='Tour.Images')),
            ],
            options={
                'managed': True,
                'db_table': 'images_user',
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('location_name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('map', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.ForeignKey(to='Tour.Districts')),
            ],
            options={
                'managed': True,
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('charge', models.FloatField()),
                ('guide', models.ForeignKey(to='Tour.Guides')),
                ('location', models.ForeignKey(to='Tour.Locations')),
            ],
            options={
                'managed': True,
                'db_table': 'manage',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('user_id', models.CharField(max_length=20)),
                ('location_id', models.CharField(max_length=20)),
                ('review', models.CharField(blank=True, max_length=300, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('travel_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('transport_type', models.CharField(max_length=20)),
                ('transport_name', models.CharField(blank=True, max_length=40, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_website', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('dest', models.ForeignKey(to='Tour.Locations', related_name='tour_travel_dest')),
                ('src', models.ForeignKey(to='Tour.Locations', related_name='tour_travel_src')),
            ],
            options={
                'managed': True,
                'db_table': 'travel',
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
                'managed': True,
                'db_table': 'users',
            },
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('user_id', 'location_id')]),
        ),
        migrations.AddField(
            model_name='imagesuser',
            name='user',
            field=models.ForeignKey(to='Tour.Users'),
        ),
        migrations.AddField(
            model_name='imageslocation',
            name='location',
            field=models.ForeignKey(to='Tour.Locations'),
        ),
        migrations.AddField(
            model_name='hotels',
            name='location',
            field=models.ForeignKey(to='Tour.Locations'),
        ),
        migrations.AddField(
            model_name='guides',
            name='image',
            field=models.ForeignKey(to='Tour.Images'),
        ),
        migrations.AddField(
            model_name='guides',
            name='location',
            field=models.ForeignKey(to='Tour.Locations'),
        ),
        migrations.AddField(
            model_name='adjacent',
            name='dest',
            field=models.ForeignKey(to='Tour.Locations', related_name='tour_adjacent_dest'),
        ),
        migrations.AddField(
            model_name='adjacent',
            name='source',
            field=models.ForeignKey(to='Tour.Locations', related_name='tour_adjacent_source'),
        ),
        migrations.AlterUniqueTogether(
            name='manage',
            unique_together=set([('location', 'guide')]),
        ),
        migrations.AlterUniqueTogether(
            name='adjacent',
            unique_together=set([('source', 'dest')]),
        ),
    ]
