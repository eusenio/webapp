# Generated by Django 3.2.9 on 2021-11-20 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211120_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_cadastro',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 20, 11, 42, 55, 356399), null=True),
        ),
    ]
