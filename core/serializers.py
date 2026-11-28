from dataclasses import asdict

from rest_framework import serializers
from .value_objects import Address


class AddressSerializerField(serializers.Field):
    def to_representation(self, value):
        return asdict(value)

    def to_internal_value(self, data):
        try:
            return Address(**data)
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        except TypeError:
            raise serializers.ValidationError('Servono "street", "city" e "zip_code".')