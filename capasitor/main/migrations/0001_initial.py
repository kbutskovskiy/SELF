# Generated by Django 4.1.3 on 2022-12-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.FloatField(verbose_name='Ёмкость')),
                ('amplitude', models.FloatField(verbose_name='Амрлитуда')),
                ('frequency', models.FloatField(verbose_name='Частота')),
            ],
        ),
    ]
