# Generated by Django 2.0.1 on 2018-03-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0004_auto_20180303_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspot',
            name='latitude',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='parkingspot',
            name='longitude',
            field=models.CharField(max_length=20),
        ),
    ]
