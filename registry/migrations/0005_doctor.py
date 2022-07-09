# Generated by Django 3.2.4 on 2021-06-26 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0004_alter_specialization_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('familyname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('firstname', models.CharField(max_length=30, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество')),
                ('active', models.BooleanField(default=1, verbose_name='Действующий')),
                ('fn', models.CharField(blank=True, max_length=200, null=True, verbose_name='Примечание')),
                ('specname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='registry.specialization', verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Справочник сотрудников',
                'db_table': 'staff',
                'ordering': ('familyname', 'firstname', 'lastname', 'specname'),
                'managed': True,
                'index_together': {('familyname', 'firstname', 'lastname', 'specname')},
            },
        ),
    ]
