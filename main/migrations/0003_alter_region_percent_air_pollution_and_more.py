# Generated by Django 4.0.3 on 2022-03-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_region_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='percent_air_pollution',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='percent_water_pollution',
            field=models.FloatField(null=True),
        ),
    ]