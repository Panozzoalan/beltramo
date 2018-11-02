# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0004_auto_20181102_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudio_medico',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='estudio',
        ),
        migrations.AddField(
            model_name='paciente',
            name='nombre',
            field=models.ForeignKey(default=1, to='laboratorio.Estudio_medico'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Estudio',
        ),
    ]
