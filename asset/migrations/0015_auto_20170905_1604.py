# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-05 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0014_gotemplaterevision'),
    ]

    operations = [
        migrations.AddField(
            model_name='goservicerevision',
            name='gotemplate_last_rev',
            field=models.IntegerField(default=1, verbose_name='gotemplate latest successful revision'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goservicerevision',
            name='last_rev',
            field=models.IntegerField(verbose_name='goproject latest successful revision'),
        ),
    ]
