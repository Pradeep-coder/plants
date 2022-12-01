# Generated by Django 4.0.3 on 2022-07-19 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantswebsite', '0010_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, verbose_name='email')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
                'ordering': ['timestamp'],
            },
        ),
    ]