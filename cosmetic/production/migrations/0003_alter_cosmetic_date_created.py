# Generated by Django 4.2.7 on 2023-12-10 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_alter_cosmetic_date_created_alter_substance_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cosmetic',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 10, 10, 34, 13, 743895, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
        ),
    ]
