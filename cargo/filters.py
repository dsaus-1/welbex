from django_filters import rest_framework as filters

from cargo.models import Cargo
from cargo.sevices import count_nearby_cars


class CargoFilter(filters.FilterSet):
    number_of_cars = filters.CharFilter(method=count_nearby_cars, name='cars')

    class Meta:
        model = Cargo
        fields = []

    def filter_miles(self, queryset, name, value):
        pks = ModelB.objects.filter(status=value).values('pk')
        return queryset.filter(pk__in=Subquery(pks))