# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_admin',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
