# Generated by Django 2.2.4 on 2020-01-05 16:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 5, 16, 33, 42, 840796, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]