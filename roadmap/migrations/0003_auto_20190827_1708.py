# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0002_users_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roadmap',
            name='steps',
        ),
        migrations.AddField(
            model_name='roadmap',
            name='steps',
            field=models.ManyToManyField(to='roadmap.Step'),
        ),
    ]
