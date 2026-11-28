from rest_framework.routers import SimpleRouter
from vehicles.views import VehicleViewSet

router = SimpleRouter()

router.register('', VehicleViewSet, basename='vehicles')

urlpatterns = router.urls