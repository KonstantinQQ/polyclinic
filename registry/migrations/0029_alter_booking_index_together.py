# Generated by Django 3.2.5 on 2021-07-10 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0028_auto_20210708_1536'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='booking',
            index_together={('appointment', 'slot')},
        ),
    ]
