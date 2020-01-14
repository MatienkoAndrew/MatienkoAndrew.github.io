# Generated by Django 2.2.4 on 2020-01-05 14:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='', max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2020, 1, 5, 14, 17, 52, 527626, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
