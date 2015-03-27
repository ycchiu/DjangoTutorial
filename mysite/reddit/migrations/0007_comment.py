# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reddit', '0006_auto_20150322_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_text', models.TextField()),
                ('published_date', models.DateTimeField(verbose_name=b'data published')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('link', models.ForeignKey(to='reddit.Link')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
