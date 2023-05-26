from geopy.distance import great_circle
from car.models import Car


def get_all_cars(cargo):
    """Метод принимает груз и возвращает список номеров всех машин с расстоянием до груза"""

    location_coordinates = (cargo.pick_up.latitude, cargo.pick_up.longitude)
    list_cars = []

    for car in Car.objects.all():
        car_coordinates = (car.location.latitude, car.location.longitude)
        distance = great_circle(location_coordinates, car_coordinates).miles
        list_cars.append({car.number: distance})

    return list_cars


def count_nearby_cars(cargo, miles=450):
    """Метод принимает груз и возвращает количество ближайших машин (дефолтное значение = 450 миль)"""

    count = sum(True for car in get_all_cars(cargo) if list(car.values())[0] <= miles)
    return count
