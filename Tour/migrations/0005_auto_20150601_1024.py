# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0004_auto_20150601_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guides',
            name='guide_email',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='hotel_email',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='restaurant_email',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transports',
            name='contact_email',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
