# Generated by Django 2.2.4 on 2020-01-05 20:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dz', '0004_auto_20200105_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 5, 20, 11, 27, 399682, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]