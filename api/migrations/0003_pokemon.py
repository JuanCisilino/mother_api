# Generated by Django 4.1.7 on 2023-07-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_doctor_historiaclinica_paciente_receta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=3000)),
                ('favorite', models.BooleanField()),
                ('types', models.CharField(max_length=3000)),
                ('evolves_to', models.CharField(max_length=3000)),
                ('evolves_from', models.CharField(max_length=3000)),
                ('base_url', models.CharField(max_length=3000)),
                ('list_img', models.CharField(max_length=3000)),
                ('det_img', models.CharField(max_length=3000)),
                ('flavor', models.CharField(max_length=3000)),
                ('strong_against', models.CharField(max_length=3000)),
                ('weak_against', models.CharField(max_length=3000)),
                ('no_damage_to', models.CharField(max_length=3000)),
                ('no_damage_from', models.CharField(max_length=3000)),
            ],
        ),
    ]