# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reddit', '0004_remove_link_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='author',
            field=models.ForeignKey(default='-1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
