from django.db import models

# Create your models here.
class ParkingSpot(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    name = models.CharField(max_length=50, blank=True)
    uuid = models.CharField(max_length=50, primary_key=True)

class State(models.Model):
    timestamp = models.DateTimeField()
    occupied = models.BooleanField()
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
