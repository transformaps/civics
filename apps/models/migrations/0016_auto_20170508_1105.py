# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 11:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0015_auto_20170504_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='address',
            field=models.CharField(help_text='Dirección de la iniciativa. No es necesario que vuelvas a introducir la ciudad de la iniciativa.', max_length=200, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='city',
            field=models.ForeignKey(help_text='Ciudad donde se encuentra la iniciativa. Si no encuentras la ciudad en el desplegable usa el botón inferior para añadir una nueva ciudad y seleccionarla', null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.City', verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='image',
            field=models.ImageField(blank=True, help_text='Sube una imagen representativa de la iniciativa haciendo click en la imagen inferior.', upload_to='images/initiatives/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='position',
            field=djgeojson.fields.PointField(help_text='Tras añadir ciudad y dirección puedes ubicar la iniciativa pulsando el botón inferior y ajustando la posición del marcador posteriormente.', null=True, verbose_name='Ubicación'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Gestor'),
        ),
    ]
