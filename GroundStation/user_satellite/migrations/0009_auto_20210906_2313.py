# Generated by Django 3.2.6 on 2021-09-06 20:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_satellite', '0008_auto_20210906_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='satellite',
            name='aop',
            field=models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AddField(
            model_name='satellite',
            name='ecc',
            field=models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AddField(
            model_name='satellite',
            name='inc',
            field=models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AddField(
            model_name='satellite',
            name='raan',
            field=models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AddField(
            model_name='satellite',
            name='sma',
            field=models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AddField(
            model_name='satellite',
            name='ta',
            field=models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
    ]