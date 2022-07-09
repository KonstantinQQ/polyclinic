# Generated by Django 3.2.5 on 2021-08-11 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0030_alter_booking_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'managed': True, 'ordering': ('familyname', 'firstname', 'lastname', 'specname'), 'verbose_name': 'Врач', 'verbose_name_plural': 'Врачи'},
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
