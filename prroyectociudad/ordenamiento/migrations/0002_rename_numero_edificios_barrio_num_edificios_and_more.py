# Generated by Django 4.0.5 on 2022-06-27 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenamiento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barrio',
            old_name='numero_edificios',
            new_name='num_edificios',
        ),
        migrations.RenameField(
            model_name='barrio',
            old_name='numero_parques',
            new_name='num_parques',
        ),
        migrations.RenameField(
            model_name='barrio',
            old_name='numero_viviendas',
            new_name='num_viviendas',
        ),
    ]