# Generated by Django 4.0.3 on 2022-07-26 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantswebsite', '0011_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='plants',
            name='original_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
