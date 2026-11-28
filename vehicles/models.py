from django.db import models
from core.fields import AddressField
from .fields import PlateField, BrandField, ModelNameField


class Vehicle(models.Model):
    brand = BrandField()
    model = ModelNameField()
    plate = PlateField(unique=True)
    address = AddressField()

    def __str__(self):
        return f"{self.brand} {self.model} - {self.plate}"




