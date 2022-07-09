# Generated by Django 3.2.5 on 2021-07-05 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registry', '0025_alter_appointment_is_slots'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'managed': True, 'verbose_name': 'Посетитель', 'verbose_name_plural': 'Посетители'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Посетитель'),
        ),
    ]