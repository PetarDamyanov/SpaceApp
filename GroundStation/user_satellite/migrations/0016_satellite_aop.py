# Generated by Django 3.2.6 on 2021-09-06 20:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_satellite', '0015_auto_20210906_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='satellite',
            name='aop',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
    ]