# Generated by Django 3.2.4 on 2021-06-28 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0008_auto_20210628_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'managed': True, 'verbose_name_plural': 'Расписание приема'},
        ),
        migrations.AddField(
            model_name='appointment',
            name='specname',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='registry.specialization', verbose_name='Специализация'),
        ),
    ]
