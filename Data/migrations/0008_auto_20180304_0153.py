# Generated by Django 2.0.1 on 2018-03-04 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0007_auto_20180303_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='occupied',
        ),
        migrations.AddField(
            model_name='state',
            name='occupied_by',
            field=models.CharField(default='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', max_length=200),
            preserve_default=False,
        ),
    ]