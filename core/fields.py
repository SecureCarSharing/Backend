import json
from dataclasses import asdict

from django.core.exceptions import ValidationError
from django.db import models
from .value_objects import Address

class AddressField(models.JSONField):
    def from_db_value(self, value, expression, connection):
        value = super().from_db_value(value, expression, connection)
        return Address(**value) if isinstance(value, dict) else value

    def to_python(self, value):
        if value is None or isinstance(value, Address):
            return value
        try:
            data = json.loads(value) if isinstance(value, str) else value
            return Address(**data)
        except ValueError as e:
            raise ValidationError(str(e)) from e
        except TypeError as e:
            raise ValidationError('Servono "street", "city" e "zip_code".') from e

    def validate(self, value, model_instance):
        super().validate(asdict(value) if isinstance(value, Address) else value, model_instance)

    def value_from_object(self, obj):
        value = super().value_from_object(obj)
        return asdict(value) if isinstance(value, Address) else value

    def get_prep_value(self, value):
        if isinstance(value, Address):
            value = asdict(value)
        return super().get_prep_value(value)

    def get_db_prep_save(self, value, connection):
        return super().get_db_prep_save(self.to_python(value), connection)