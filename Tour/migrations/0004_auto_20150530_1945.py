# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0003_auto_20150530_1929'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='users',
            unique_together=set([('user_email',)]),
        ),
    ]
