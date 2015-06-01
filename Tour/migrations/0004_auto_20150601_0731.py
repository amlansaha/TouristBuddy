# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0003_auto_20150601_0406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transports',
            name='contact_info',
        ),
        migrations.RemoveField(
            model_name='transports',
            name='contact_web',
        ),
        migrations.AddField(
            model_name='restaurants',
            name='restaurant_cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transports',
            name='transport_name',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
    ]
