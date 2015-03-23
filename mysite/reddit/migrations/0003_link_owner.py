# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reddit', '0002_auto_20150314_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='owner',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
    ]
