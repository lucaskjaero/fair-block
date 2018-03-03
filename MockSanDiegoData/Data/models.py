from django.db import models

# Create your models here.
class ParkingSpot(models.Model):
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    token = models.CharField(max_length=50)

class State(models.Model):
    timestamp = models.DateTimeField()
    occupied = models.BooleanField()
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
