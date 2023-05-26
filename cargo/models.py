from django.db import models
from django.utils.translation import gettext as _
from location.models import Location
from django.core.validators import MaxValueValidator, MinValueValidator


class Cargo(models.Model):
    """Модель грузов"""

    pick_up = models.ForeignKey(Location, related_name='cargo_pick_up', on_delete=models.PROTECT,
                                verbose_name=_('локация pick-up'))
    delivery = models.ForeignKey(Location, related_name='cargo_delivery', on_delete=models.PROTECT,
                                 verbose_name=_('локация delivery'))
    weight = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(1)], verbose_name=_('Вес'))
    description = models.TextField(verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Груз')
        verbose_name_plural = _('Грузы')

    def __str__(self):
        return f'{self.pk} {self.description[:15]}'
