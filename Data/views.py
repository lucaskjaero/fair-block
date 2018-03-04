from django.shortcuts import render

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
