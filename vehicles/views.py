from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .value_objects import Brand, ModelName, Plate
from .models import Vehicle
from .serializer import VehicleSerializer

FILTERS = {
    "brand": Brand,
    "model": ModelName,
    "plate": Plate,
}


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params
        for param, value_class in FILTERS.items():
            if param in params:
                try:
                    queryset = queryset.filter(**{param: value_class(params[param])})
                except ValueError as e:
                    raise ValidationError({param: str(e)})
        return queryset