# Generated by Django 4.2.5 on 2023-11-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCI', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reglas',
            new_name='Regla',
        ),
        migrations.AddField(
            model_name='equipo',
            name='alianzas',
            field=models.ManyToManyField(to='TCI.alianza'),
        ),
    ]
