from django.db import models
from django.db.models.fields.related import ForeignKey


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    registered = models.DateField(auto_now=True)
    salt = models.CharField(max_length=250)
    def __str__(self):
        return f'{self.username}, {self.password}, {self.salt}'
    
    def getPass(self):
        return self.password
    
    def getSalt(self):
        return self.salt

class Satellite(models.Model):
    norad_id = models.CharField(max_length=250, primary_key=True)
    frequency = models.FloatField()
    protocol = models.CharField(max_length=250)
    status = models.CharField(max_length=250 ,default="active", choices=[('on', "active"),('off', "dead")])
    registered = models.DateField(auto_now=True)

class User_satellite(models.Model):
    users_id=models.ForeignKey(User, on_delete=models.CASCADE)
    satellite_id=models.ForeignKey(Satellite, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.users_id} - {self.satellite_id}'