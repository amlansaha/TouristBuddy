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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance_in_km', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'adjacent',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('dist_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('dist_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'districts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Guides',
            fields=[
                ('guide_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('guide_name', models.CharField(max_length=80)),
                ('contact_no', models.CharField(max_length=20)),
                ('guide_email', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'guides',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('hotel_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('hotel_name', models.CharField(max_length=50)),
                ('hotel_website', models.CharField(max_length=50, null=True, blank=True)),
                ('hotel_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('hotel_email', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'hotels',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('image_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('image_dir', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'images',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImagesGuide',
            fields=[
                ('id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('guide', models.ForeignKey(to='Tour.Guides')),
                ('image', models.ForeignKey(to='Tour.Images')),
            ],
            options={
                'db_table': 'images_guide',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImagesLocation',
            fields=[
                ('id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('image', models.ForeignKey(to='Tour.Images')),
            ],
            options={
                'db_table': 'images_location',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImagesUser',
            fields=[
                ('id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('image', models.ForeignKey(to='Tour.Images')),
            ],
            options={
                'db_table': 'images_user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('location_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('map', models.CharField(max_length=20, null=True, blank=True)),
                ('dist', models.ForeignKey(to='Tour.Districts')),
            ],
            options={
                'db_table': 'locations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('charge', models.FloatField()),
                ('guide', models.ForeignKey(to='Tour.Guides')),
                ('location', models.ForeignKey(to='Tour.Locations')),
            ],
            options={
                'db_table': 'manage',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('restaurant_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('restaurant_name', models.CharField(max_length=50)),
                ('restaurant_website', models.CharField(max_length=50, null=True, blank=True)),
                ('restaurant_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('restaurant_email', models.CharField(max_length=20, null=True, blank=True)),
                ('location', models.ForeignKey(to='Tour.Locations')),
            ],
            options={
                'db_table': 'restaurants',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.CharField(max_length=300, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('location', models.ForeignKey(to='Tour.Locations')),
            ],
            options={
                'db_table': 'review',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Spots',
            fields=[
                ('spot_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('spot_name', models.CharField(max_length=50)),
                ('location', models.ForeignKey(related_name='tour_spots_location', to='Tour.Locations')),
            ],
            options={
                'db_table': 'spots',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transports',
            fields=[
                ('transport_id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('transport_type', models.CharField(max_length=3)),
                ('contact_info', models.CharField(max_length=200, null=True)),
                ('contact_web', models.CharField(max_length=40, null=True)),
                ('contact_phone', models.CharField(max_length=20, null=True)),
                ('contact_email', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'transports',
            },
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fare', models.IntegerField(null=True)),
                ('destination_id1', models.ForeignKey(related_name='destination1', to='Tour.Locations')),
                ('source_id1', models.ForeignKey(related_name='source1', to='Tour.Locations')),
                ('transport', models.ForeignKey(to='Tour.Transports')),
            ],
            options={
                'db_table': 'travel',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('user_email', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to='Tour.Users'),
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
            field=models.ForeignKey(related_name='tour_adjacent_dest', to='Tour.Locations'),
        ),
        migrations.AddField(
            model_name='adjacent',
            name='source',
            field=models.ForeignKey(related_name='tour_adjacent_source', to='Tour.Locations'),
        ),
        migrations.AlterUniqueTogether(
            name='travel',
            unique_together=set([('source_id1', 'destination_id1', 'transport')]),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('user', 'location')]),
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
