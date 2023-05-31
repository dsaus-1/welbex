from rest_framework.routers import SimpleRouter

from cargo.apps import CargoConfig
from cargo.views import CargoModelViewSet

app_name = CargoConfig.name


router = SimpleRouter()
router.register('', CargoModelViewSet, basename='cargo_reg')

urlpatterns = router.urls