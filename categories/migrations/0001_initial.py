# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=512)),
                ('parent_name', models.CharField(max_length=512)),
                ('budget', models.FloatField()),
                ('amount', models.FloatField()),
                ('date_of_budget', models.DateField()),
                ('date_of_amount', models.DateField()),
                ('type', models.CharField(max_length=16)),
                ('level', models.IntegerField()),
            ],
        ),
    ]
