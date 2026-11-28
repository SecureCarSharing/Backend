from rest_framework import serializers
from vehicles.models import Vehicle
from core.serializers import AddressSerializerField

class VehicleSerializer(serializers.ModelSerializer):
    address = AddressSerializerField()

    class Meta:
        model = Vehicle
        fields = ["id", "plate", "model", "address", "brand"]