from django.db import models
from django.utils.translation import gettext as _


class Location(models.Model):
    """Модель локаций"""

    city = models.CharField(max_length=50, verbose_name=_('Город'))
    state = models.CharField(max_length=50, verbose_name=_('Штат'))
    postal_code = models.IntegerField(unique=True, verbose_name=_('Почтовый индекс'))
    latitude = models.DecimalField(max_digits=12, decimal_places=6, verbose_name=_('Широта'))
    longitude = models.DecimalField(max_digits=12, decimal_places=6, verbose_name=_('Долгота'))


    class Meta:
        verbose_name = _('Локация')
        verbose_name_plural = _('Локации')

    def __str__(self):
        return f'{self.city}'
