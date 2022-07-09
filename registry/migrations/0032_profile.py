# Generated by Django 3.2.5 on 2021-08-11 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registry', '0031_auto_20210811_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('gender', models.CharField(choices=[('Н', 'Неопределенный'), ('Ж', 'Женский'), ('М', 'Мужской')], max_length=1, verbose_name='Пол')),
                ('patronymic', models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Посетитель')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи (дополнение)',
                'db_table': 'profile',
                'managed': True,
            },
        ),
    ]