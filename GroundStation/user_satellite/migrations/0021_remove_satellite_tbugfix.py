# Generated by Django 3.2.6 on 2021-09-06 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_satellite', '0020_auto_20210906_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='satellite',
            name='tbugfix',
        ),
    ]
