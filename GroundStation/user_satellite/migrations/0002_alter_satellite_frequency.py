# Generated by Django 4.0.dev20210830100804 on 2021-09-04 15:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_satellite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='frequency',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)]),
        ),
    ]