from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from cargo.models import Cargo
from cargo.sevices import get_all_cars, count_nearby_cars
from location.models import Location


class CargoSerializer(serializers.ModelSerializer):
    pick_up = SlugRelatedField(slug_field="postal_code", queryset=Location.objects.all())
    delivery = SlugRelatedField(slug_field="postal_code", queryset=Location.objects.all())

    class Meta:
        model = Cargo
        fields = (
            'id',
            'pick_up',
            'delivery',
            'weight',
            'description',
        )


class CargoListSerializer(serializers.ModelSerializer):
    number_of_cars = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = (
            'pick_up',
            'delivery',
            'number_of_cars',
        )

    def get_number_of_cars(self, cargo):
        request = self.context.get('request')
        q_string = request._request.environ.get('QUERY_STRING')
        if q_string:
            q_dict = dict(filter_.split('=') for filter_ in q_string.split('&'))

            miles = q_dict.get('miles')
            if miles:
                return count_nearby_cars(cargo, int(miles))

        return count_nearby_cars(cargo)


class CargoRetrieveSerializer(serializers.ModelSerializer):
    cars = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = (
            'pick_up',
            'delivery',
            'weight',
            'description',
            'cars',
        )

    def get_cars(self, cargo):
        return get_all_cars(cargo)


class CargoUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cargo
        fields = (
            'weight',
            'description',
        )