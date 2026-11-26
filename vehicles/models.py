from django.db import models
from core.fields import AddressField
from .validators import validate_brand

class Vehicle(models.Model):
    brand = models.CharField(max_length=100, validators=[validate_brand])
    model = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    address = AddressField()