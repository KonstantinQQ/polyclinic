# Generated by Django 3.2.4 on 2021-06-28 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0006_alter_doctor_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='lastname',
            field=models.CharField(default='-', max_length=30, verbose_name='Отчество'),
        ),
    ]
