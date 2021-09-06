from django.db import models
from django.db.models.fields.related import ForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    registered = models.DateField(auto_now=True)
    salt = models.CharField(max_length=250)
    def __str__(self):
        return f''
    
    def getPass(self):
        return self.password
    
    def getSalt(self):
        return self.salt

class Satellite(models.Model):
    norad_id = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250, default = '')
    frequency = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)],)
    protocol = models.CharField(max_length=250)
    sma = models.FloatField(validators=[MinValueValidator(-100000.0), MaxValueValidator(100000.0)],default=0)
    inc = models.FloatField(validators=[MinValueValidator(-100000.0), MaxValueValidator(100000.0)],default=0)
    raan = models.FloatField(validators=[MinValueValidator(-100000.0), MaxValueValidator(100000.0)],default=0)
    aop = models.FloatField(validators=[MinValueValidator(-100000.0), MaxValueValidator(100000.0)],default=0)
    ecc = models.FloatField(validators=[MinValueValidator(-100000.0), MaxValueValidator(100000.0)],default=0)
    ta = models.FloatField(validators=[MinValueValidator(-100000.0), MaxValueValidator(100000.0)],default=0)
    status = models.CharField(max_length=250,default="active", choices=[('on', "active"),('off', "dead")])
    registered = models.DateField(auto_now=True)

    def getNorad(self):
        return self.norad_id
    
    def __str__(self):
        return f"{self.norad_id}"
    
    def __repr__(self):
        return f"{self.norad_id}"

class User_satellite(models.Model):
    users_id=models.ForeignKey(User, on_delete=models.CASCADE)
    satellite_id=models.ForeignKey(Satellite, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.users_id} - {self.satellite_id}'