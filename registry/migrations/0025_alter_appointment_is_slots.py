# Generated by Django 3.2.5 on 2021-07-05 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0024_appointment_is_slots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='is_slots',
            field=models.BooleanField(default=False, verbose_name='Слоты'),
        ),
    ]
