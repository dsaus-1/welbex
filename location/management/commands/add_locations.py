from django.core.management import BaseCommand
import csv
from config.settings import BASE_DIR
from location.models import Location


class Command(BaseCommand):
    """Добавление локаций из CSV в DB"""

    def handle(self, *args, **options):
        Location.objects.all().delete()

        list_locations = []

        with open(f'{BASE_DIR}/uszips.csv', encoding='utf-8') as open_file:
            read_open_file = csv.DictReader(open_file)

            for num, location in enumerate(read_open_file, start=1):
                list_locations.append(Location(num, location.get('city'), location.get('state_name'),
                                               location.get('zip'), location.get('lat'),
                                               location.get('lng')))

            Location.objects.bulk_create(list_locations)

