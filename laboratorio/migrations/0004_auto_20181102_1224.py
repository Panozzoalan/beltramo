# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0003_auto_20181022_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('estudio', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='estudio',
            field=models.ForeignKey(default=1, to='laboratorio.Estudio'),
            preserve_default=False,
        ),
    ]
