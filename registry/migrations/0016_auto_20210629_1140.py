# Generated by Django 3.2.4 on 2021-06-29 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0015_alter_appointment_dapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='planbudget',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Бюджет'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='plancommerce',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Внебюджет'),
        ),
    ]
