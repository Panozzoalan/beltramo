# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0005_auto_20181102_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='nombre',
            new_name='estudio',
        ),
    ]
