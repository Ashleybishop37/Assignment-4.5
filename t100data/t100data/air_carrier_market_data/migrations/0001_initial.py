# Generated by Django 3.0.10 on 2020-10-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('passengers', models.IntegerField()),
                ('freight', models.IntegerField()),
                ('mail', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('carrier_id', models.CharField(max_length=3)),
                ('carrier_name', models.TextField()),
                ('orig_airport_id', models.IntegerField()),
                ('orig_iata_code', models.CharField(max_length=3)),
                ('orig_city_name', models.TextField()),
                ('orig_state_abr', models.TextField(max_length=2)),
                ('dest_airport_id', models.IntegerField()),
                ('dest_iata_code', models.CharField(max_length=3)),
                ('dest_city_name', models.TextField()),
                ('dest_state_abr', models.TextField(max_length=2)),
                ('month', models.IntegerField(default=0)),
            ],
        ),
    ]
