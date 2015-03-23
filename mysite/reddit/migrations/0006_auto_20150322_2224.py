# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0005_link_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='downvote',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='link',
            name='upvote',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
