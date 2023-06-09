from datetime import datetime, timedelta

import pytz
from django.core.management import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from config import settings


class Command(BaseCommand):
    """Создание задачи на обновление локации машин"""

    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=3,
            period=IntervalSchedule.MINUTES,
        )


        PeriodicTask.objects.create(
            interval=schedule,  # we created this above.
            name='Refresh car location',  # simply describes this periodic task.
            task='car.tasks.updating_locations',  # name of task.
            expires=datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=365)
        )