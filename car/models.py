from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from location.models import Location


class Car(models.Model):
    """Модель машин"""

    number = models.CharField(max_length=5, unique=True, verbose_name=_('Номер'))
    location = models.ForeignKey(Location, related_name='car', on_delete=models.PROTECT, verbose_name=_('Локация'))
    load_capacity = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(1)],
                                        verbose_name=_('Грузоподъёмность'))


    class Meta:
        verbose_name = _('Машина')
        verbose_name_plural = _('Машины')

    def __str__(self):
        return f'{self.number}'