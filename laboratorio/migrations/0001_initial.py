# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio_medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_apellido', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('especialidad', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_apellido', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='estudio_medico',
            name='medico',
            field=models.ManyToManyField(to='laboratorio.Medico'),
        ),
        migrations.AddField(
            model_name='estudio_medico',
            name='paciente',
            field=models.ForeignKey(to='laboratorio.Paciente'),
        ),
    ]
