# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 05:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20170228_0555'),
        ('flows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flow',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='flows', to='projects.Project'),
            preserve_default=False,
        ),
    ]
