# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('especializacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='medico',
            old_name='nombre_apellido',
            new_name='nombre_y_apellido',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='nombre_apellido',
            new_name='nombre_y_apellido',
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidad',
            field=models.ForeignKey(to='laboratorio.Especialidad'),
        ),
    ]
