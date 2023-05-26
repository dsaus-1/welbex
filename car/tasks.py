from random import randint

from celery import shared_task

from car.models import Car
from location.models import Location


@shared_task
def updating_locations():
    """Обновляет локации машин на другую случайную"""

    cars_queryset = Car.objects.all()
    locations_queryset = Location.objects.all()
    last_location = len(locations_queryset) - 1

    for car in cars_queryset:
        new_location = randint(0, last_location)

        if car.location.pk == locations_queryset[new_location].pk:
            if new_location < last_location:
                new_location += 1
            else:
                new_location -= 1

        car.location = locations_queryset[new_location]
        car.save()