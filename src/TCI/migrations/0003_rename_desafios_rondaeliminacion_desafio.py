# Generated by Django 4.2.7 on 2023-11-24 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TCI', '0002_remove_desafio_reglas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rondaeliminacion',
            old_name='desafios',
            new_name='desafio',
        ),
    ]
