# Generated by Django 4.2.5 on 2023-11-10 12:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCI', '0002_rename_reglas_regla_equipo_alianzas'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='foto',
            field=models.ImageField(default='static/img/02', upload_to='img/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
        migrations.AddField(
            model_name='participante',
            name='foto',
            field=models.ImageField(default='static/img/01', upload_to='img/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
        migrations.AddField(
            model_name='temporada',
            name='foto',
            field=models.ImageField(default='static/img/03', upload_to='img/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]
