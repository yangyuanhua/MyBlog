# Generated by Django 2.0 on 2020-05-27 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 27, 6, 55, 55, 913885, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
