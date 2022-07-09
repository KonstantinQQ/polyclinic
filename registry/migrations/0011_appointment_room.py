# Generated by Django 3.2.4 on 2021-06-29 04:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0010_alter_appointment_specname'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='room',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Кабинет'),
        ),
    ]
