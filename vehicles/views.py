from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Vehicle
from .serializer import VehicleSerializer
from vehicles.filters import VehicleFilter

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VehicleFilter