# Generated by Django 3.2.6 on 2021-09-06 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_satellite', '0006_auto_20210906_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='aop',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='ecc',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='inc',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='raan',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='sma',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='ta',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-100000.0), django.core.validators.MaxValueValidator(100000.0)]),
        ),
    ]
