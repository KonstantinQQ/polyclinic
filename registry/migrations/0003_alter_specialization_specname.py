# Generated by Django 3.2.4 on 2021-06-25 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_alter_specialization_specname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialization',
            name='specname',
            field=models.CharField(max_length=30, unique=True, verbose_name='Специализация'),
        ),
    ]
