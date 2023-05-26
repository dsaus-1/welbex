from rest_framework import generics

from car.models import Car
from car.serializers import CarSerializer


class CarUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
