from django.db import models
from django.utils.translation import gettext as _


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Название'))
    description = models.CharField(max_length=350, verbose_name=_('Описание'))
    price = models.FloatField(verbose_name=_('Цена'))


    class Meta:
        verbose_name = _('Предмет')
        verbose_name_plural = _('Предметы')

    def __str__(self):
        return f'{self.name}'