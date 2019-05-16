from django.conf import settings
from django.db import models
from geekshop.settings import AUTH_USER_MODEL
from mainapp.models import Good


def _format_price(price):
    return '{:,.2f}'.format(price).replace(',', ' ').replace('.', ',')+' руб.'


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='basket', on_delete=models.CASCADE)
    good = models.ForeignKey(
        'mainapp.Good', related_name='good', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        verbose_name="количество", default=0)
    add_datetime = models.DateTimeField(
        verbose_name="время", auto_now_add=True)

    def get_total_price(self):
        return _format_price(self.quantity * self.good.price)

    def get_all_total_price(self):
        basket = Basket.objects.filter(user=self.user)
        total_price = float(0)
        for item in basket:
            total_price += item.quantity * item.good.price
        return _format_price(total_price)

    def get_all_total_quantity(self):
        basket = Basket.objects.filter(user=self.user)
        total_quantity = 0
        for item in basket:
            total_quantity += item.quantity
        return total_quantity
