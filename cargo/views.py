from rest_framework import viewsets

from cargo.models import Cargo
from cargo.serializers import CargoSerializer, CargoListSerializer, CargoRetrieveSerializer, CargoUpdateSerializer


class CargoModelViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    filterset_fields = ["weight"]

    def get_serializer_class(self):
        if self.action == 'list':
            return CargoListSerializer
        elif self.action == 'create':
            return CargoSerializer
        elif self.action == 'retrieve':
            return CargoRetrieveSerializer
        elif self.action == 'update':
            return CargoUpdateSerializer
