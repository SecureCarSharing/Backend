from rest_framework import serializers
from vehicles.models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Vehicle