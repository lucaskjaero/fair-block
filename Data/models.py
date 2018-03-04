from django.db import models

# Create your models here.
class ParkingSpot(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    name = models.CharField(max_length=50, blank=True)
    uuid = models.CharField(max_length=50, primary_key=True)

class State(models.Model):
    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
    occupied_by = models.CharField(max_length=200)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
