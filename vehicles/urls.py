from rest_framework.routers import SimpleRouter
from rest_framework import viewsets
from vehicles.models import Vehicle
from vehicles.views import VehicleViewSet

router = SimpleRouter()

router.register('', VehicleViewSet, basename='vehicles')

urlpatterns = router.urls