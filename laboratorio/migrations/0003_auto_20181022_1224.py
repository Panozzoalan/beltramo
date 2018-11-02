# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_auto_20180823_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='dni',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='medico',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
    ]
