from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
from rest_framework import viewsets
from .models import ParkingSpot, State
from .serializers import ParkingSpotSerializer, StateSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

class StateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = StateSerializer

    def get_queryset(self):
        spot = self.kwargs['spot']
        return State.objects.filter(parking_spot=spot)

class EmptyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ParkingSpotSerializer
    queryset = ParkingSpot.objects.exclude(state__time_out__isnull=True)

class FullViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ParkingSpotSerializer
    queryset = ParkingSpot.objects.filter(state__time_out__isnull=True)
