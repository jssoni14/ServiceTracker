# Generated by Django 2.1.2 on 2018-11-26 23:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trax', '0003_auto_20181124_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
