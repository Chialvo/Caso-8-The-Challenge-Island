# Generated by Django 4.2.7 on 2023-11-24 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCI', '0005_alter_temporada_listarondaeliminacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temporada',
            name='listaAlianza',
        ),
        migrations.AddField(
            model_name='temporada',
            name='listaAlianzas',
            field=models.ManyToManyField(blank=True, to='TCI.alianza'),
        ),
    ]