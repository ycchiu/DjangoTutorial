# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0003_link_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='owner',
        ),
    ]
