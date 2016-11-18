# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 11:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('solaris', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 18, 11, 54, 26, 377290, tzinfo=utc), editable=False, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateTimeField(verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=160, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateTimeField(verbose_name='Start date'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 18, 11, 54, 26, 377290, tzinfo=utc), editable=False, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='end_date',
            field=models.DateTimeField(verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=160, verbose_name='Topic Name'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='start_date',
            field=models.DateTimeField(verbose_name='Start date'),
        ),
    ]
