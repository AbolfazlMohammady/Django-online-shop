from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False, verbose_name=_('Is Paid'))

    first_name = models.CharField(max_length=100 , verbose_name=_('first_name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last_name'))
    phone = models.CharField(max_length=11, verbose_name=_('phone'))
    address = models.CharField(max_length=700, verbose_name=_('adress'))
    order_note = models.CharField(max_length=700, verbose_name=_('Order Note'), blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)  
    datetime_modified = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f'order {self.id}'
    
    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'))
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name=_('quantity'))
    price = models.PositiveIntegerField(verbose_name=_('price'))

    def __str__(self):
        return f"order item {self.id} or order{self.order.id}"
