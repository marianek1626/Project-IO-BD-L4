# Generated by Django 3.0.6 on 2020-06-03 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_sala_zdjecie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rezerwacja',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='rezerwacja',
            name='event_name',
        ),
        migrations.RemoveField(
            model_name='rezerwacja',
            name='event_type',
        ),
        migrations.RemoveField(
            model_name='rezerwacja',
            name='start_date',
        ),
    ]