# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('user_id', models.UUIDField(serialize=False, primary_key=True, editable=False, default=uuid.uuid4)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('birthday', models.DateField(null=True, blank=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoadMap',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('explanation', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='roadmap',
            name='steps',
            field=models.ForeignKey(to='roadmap.Step', on_delete=django.db.models.deletion.DO_NOTHING, related_name='steps'),
        ),
        migrations.AddField(
            model_name='project',
            name='roadmap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='roadmap.RoadMap'),
        ),
    ]
