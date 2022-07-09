# Generated by Django 3.2.4 on 2021-06-30 04:45

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0016_auto_20210629_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appbegin',
            field=models.TimeField(choices=[(datetime.time(7, 0), '07:00'), (datetime.time(8, 0), '08:00'), (datetime.time(9, 0), '09:00'), (datetime.time(10, 0), '10:00'), (datetime.time(11, 0), '11:00'), (datetime.time(12, 0), '12:00'), (datetime.time(13, 0), '13:00'), (datetime.time(14, 0), '14:00'), (datetime.time(15, 0), '15:00'), (datetime.time(16, 0), '16:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(19, 0), '19:00'), (datetime.time(20, 0), '20:00')], verbose_name='Начало'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='append',
            field=models.TimeField(choices=[(datetime.time(7, 0), '07:00'), (datetime.time(8, 0), '08:00'), (datetime.time(9, 0), '09:00'), (datetime.time(10, 0), '10:00'), (datetime.time(11, 0), '11:00'), (datetime.time(12, 0), '12:00'), (datetime.time(13, 0), '13:00'), (datetime.time(14, 0), '14:00'), (datetime.time(15, 0), '15:00'), (datetime.time(16, 0), '16:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(19, 0), '19:00'), (datetime.time(20, 0), '20:00')], verbose_name='Окончание'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='dapp',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2021, 7, 1))], verbose_name='День приема'),
        ),
    ]
