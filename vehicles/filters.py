import django_filters
from vehicles.models import Vehicle

class VehicleFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(lookup_expr="icontains")
    model = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Vehicle
        fields = ["brand", "model"]