# Generated by Django 3.2.4 on 2021-06-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialization',
            name='specname',
            field=models.CharField(db_index=True, max_length=30, unique=True, verbose_name='Специализация'),
        ),
    ]
