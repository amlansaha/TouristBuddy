# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0002_users_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='hotel_cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
