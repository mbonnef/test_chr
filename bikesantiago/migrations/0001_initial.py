# Generated by Django 4.1.7 on 2023-02-18 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('ultima_actualizacion', models.DateTimeField()),
                ('direccion', models.CharField(max_length=80)),
                ('codigo_postal', models.CharField(max_length=80)),
                ('slots', models.IntegerField()),
                ('cant_bicicletas_n', models.IntegerField()),
                ('bicicletas_e', models.BooleanField()),
                ('cant_bicicletas_e', models.IntegerField()),
                ('arrendando', models.IntegerField()),
                ('devolviendo', models.IntegerField()),
                ('terminal_pago', models.BooleanField(max_length=80)),
                ('formas_pago', models.CharField(max_length=80)),
            ],
        ),
    ]
