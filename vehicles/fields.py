from django.core.exceptions import ValidationError
from django.db import models
from .value_objects import Brand, ModelName, Plate

class ValueObjectField(models.Field):
    value_class = None
    attr = None
    length = None

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = self.length
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"

    def from_db_value(self, value, expression, connection):
        return None if value is None else self.value_class(value)

    def to_python(self, value):
        if value is None or isinstance(value, self.value_class):
            return value
        try:
            return self.value_class(value)
        except ValueError as e:
            raise ValidationError(str(e)) from e

    def get_prep_value(self, value):
        obj = self.to_python(value)
        return None if obj is None else getattr(obj, self.attr)


class PlateField(ValueObjectField):
    value_class, attr, length = Plate, "number", 7


class BrandField(ValueObjectField):
    value_class, attr, length = Brand, "name", 30


class ModelNameField(ValueObjectField):
    value_class, attr, length = ModelName, "name", 50