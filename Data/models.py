from django.db import models


class ParkingSpot(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)

    price = models.DecimalField(max_digits=5, decimal_places=2)
    max_hours = models.IntegerField()

    name = models.CharField(max_length=50, blank=True)
    uuid = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.uuid)


class State(models.Model):
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(blank=True)
    occupied_by = models.CharField(max_length=200)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
