# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='published_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='link',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
