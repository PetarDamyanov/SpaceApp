from django.db import models
from django.http import response
from user_satellite.models import User, Satellite

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    satellite_id = models.ForeignKey(Satellite, on_delete=models.CASCADE)
    begin = models.DateTimeField()
    end = models.DateTimeField()

class Command(models.Model):
    id = models.AutoField(primary_key=True)
    command = models.TextField()
    date_time = models.DateTimeField()

class Response(models.Model):
    id = models.AutoField(primary_key=True)
    response = models.TextField()
    date_time = models.DateTimeField()

class Communication(models.Model):
    id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    command_id = models.ForeignKey(Command, on_delete=models.CASCADE)
    response_id = models.ForeignKey(Response, on_delete=models.CASCADE)

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    waterfall = models.TextField()
    decoded = models.TextField()
    processed = models.TextField()