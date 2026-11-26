import json
from django.db import models
from .value_objects import Address

class AddressField(models.JSONField):
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        data = json.loads(value) if isinstance(value, str) else value
        return Address(**data)

    def to_python(self, value):
        if isinstance(value, Address) or value is None:
            return value
        data = json.loads(value) if isinstance(value, str) else value
        return Address(**data)

    def get_prep_value(self, value):
        if isinstance(value, Address):
            value = {
                "street": value.street,
                "city": value.city,
                "zip_code": value.zip_code,
            }
        return super().get_prep_value(value)