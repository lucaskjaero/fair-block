# Generated by Django 2.0.1 on 2018-03-03 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingspot',
            name='token',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]