# Generated by Django 5.1.7 on 2025-03-09 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0004_alter_medico_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='medico',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='medico',
            name='video',
        ),
    ]
