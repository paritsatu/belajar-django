# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-17 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import edit.validatorsn


class Migration(migrations.Migration):

    dependencies = [
        ('baca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='body',
            field=models.TextField(validators=[edit.validatorsn.validate_body]),
        ),
        migrations.AlterField(
            model_name='artikel',
            name='penulis',
            field=models.CharField(max_length=20, validators=[edit.validatorsn.validate_author]),
        ),
    ]
