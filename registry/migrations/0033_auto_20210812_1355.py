# Generated by Django 3.2.5 on 2021-08-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0032_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'managed': True, 'verbose_name': 'Пользователь (сотрудник, посетитель)', 'verbose_name_plural': 'Пользователи (дополнение)'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='patronymic',
            field=models.CharField(default='-', max_length=30, null=True, verbose_name='Отчество'),
        ),
    ]