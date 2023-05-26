from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from car.models import Car
from location.models import Location


class CarSerializer(serializers.ModelSerializer):
    location = SlugRelatedField(slug_field="postal_code", queryset=Location.objects.all())

    class Meta:
        model = Car
        fields = (
            'number',
            'location',
            'load_capacity',
        )