# Generated by Django 4.1.7 on 2023-12-21 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='usuario',
            new_name='idusuario',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='usuario',
            new_name='idusuario',
        ),
    ]
