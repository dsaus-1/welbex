from django.urls import path

from car.apps import CarConfig
from car.views import CarUpdateAPIView

app_name = CarConfig.name


urlpatterns = [
    path('update/<int:pk>/', CarUpdateAPIView.as_view(), name='update'),
]