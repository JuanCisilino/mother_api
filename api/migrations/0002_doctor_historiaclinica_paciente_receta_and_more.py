# Generated by Django 4.1.7 on 2023-02-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.TextField(max_length=8)),
                ('matricula', models.PositiveIntegerField()),
                ('firma_url', models.TextField(max_length=200)),
                ('photo_url', models.TextField(max_length=200)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pdf', models.CharField(max_length=30)),
                ('dni_paciente', models.PositiveIntegerField()),
                ('doctor', models.IntegerField()),
                ('timestamp', models.PositiveBigIntegerField()),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nombre', models.CharField(max_length=30)),
                ('dni', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('dj_url', models.CharField(max_length=200)),
                ('afiliado', models.IntegerField()),
                ('doctor', models.IntegerField()),
                ('descripcion', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pdf', models.CharField(max_length=30)),
                ('dni_paciente', models.PositiveIntegerField()),
                ('doctor', models.IntegerField()),
                ('timestamp', models.PositiveBigIntegerField()),
                ('descripcion', models.CharField(max_length=600)),
                ('generico', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VademecumGenerico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('doctor', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VademecumMarca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('doctor', models.PositiveIntegerField()),
            ],
        ),
    ]
