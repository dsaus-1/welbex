from django.core.management import BaseCommand
from random import shuffle, randint
import string

from django.shortcuts import get_object_or_404

from car.models import Car
from location.models import Location


class Command(BaseCommand):
    """Добавление 20 машин в DB"""

    def handle(self, *args, **options):
        list_cars = []

        numbers = [i for i in range(1000, 9999)]
        litters = list(string.ascii_uppercase)
        shuffle(numbers)
        shuffle(litters)

        number_locations = Location.objects.count()

        for num in range(1, 21):
            location = get_object_or_404(Location, pk=randint(1, number_locations))

            list_cars.append(Car(num, f'{numbers[num]}{litters[num]}', location.pk, randint(1, 1000)))

        Car.objects.bulk_create(list_cars)

