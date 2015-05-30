# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tour', '0002_auto_20150530_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_email',
            field=models.CharField(error_messages={'duplicate': 'This email has already been used.'}, max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='users',
            unique_together=set([]),
        ),
    ]
