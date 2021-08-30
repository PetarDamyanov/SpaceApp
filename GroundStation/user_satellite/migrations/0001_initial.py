# Generated by Django 4.0.dev20210823042207 on 2021-08-30 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('norad_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('frequency', models.FloatField()),
                ('protocol', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('on', 'active'), ('off', 'dead')], default='active', max_length=250)),
                ('registered', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('registered', models.DateField(auto_now=True)),
                ('salt', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='User_satellite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satellite_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_satellite.satellite')),
                ('users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_satellite.user')),
            ],
        ),
    ]
