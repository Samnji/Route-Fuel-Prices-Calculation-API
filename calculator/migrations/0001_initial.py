# Generated by Django 3.2.23 on 2024-12-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis_truckstop_id', models.IntegerField(unique=True)),
                ('truckstop_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('rack_id', models.IntegerField()),
                ('retail_price', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
        migrations.AddIndex(
            model_name='fuelprice',
            index=models.Index(fields=['city', 'state'], name='calculator__city_35eba4_idx'),
        ),
        migrations.AddIndex(
            model_name='fuelprice',
            index=models.Index(fields=['retail_price'], name='calculator__retail__c6624b_idx'),
        ),
    ]