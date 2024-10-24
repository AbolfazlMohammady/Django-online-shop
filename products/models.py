from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from ckeditor import fields


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Category Name'))

    def __str__(self):
        return self.name


class Color(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    

class Discount(models.Model):
    discount = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.discount)


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = fields.RichTextField(verbose_name=_('Description')) 
    short_description = models.TextField(verbose_name=_('Short Description'), blank=True)
    price = models.PositiveIntegerField(default=0, verbose_name=_('Price'))  
    active = models.BooleanField(default=True, verbose_name=_('Active')) 
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='product/product_cover')
    size = models.CharField(max_length=255, blank=True)
    weight = models.CharField(max_length=255, blank=True)

    category = models.ManyToManyField(Category, related_name='products')
    color = models.ManyToManyField(Color, blank=True ,related_name='products')
    discount = models.ForeignKey(Discount, blank=True ,null=True, on_delete=models.CASCADE)

    datetime_created = models.DateTimeField(default=timezone.now , verbose_name=_('Date Created'))  
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date Modified'))  

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.pk])
    
    def get_discount_price(self):
        """محاسبه قیمت تخفیف‌دار یا بازگرداندن قیمت اصلی"""
        if self.discount:
            discount_percentage = self.discount.discount
            discount_amount = self.price * (discount_percentage / 100)
            return int(self.price - discount_amount)
        return self.price


class ActiveCommentsManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(active=True)

class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _("Very Bad")),  
        ('2', _('Bad')),  
        ('3', _('Normal')),  
        ('4', _('Good')), 
        ('5', _('Perfect')),  
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Product'))  
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Author'))  
    body = models.TextField(verbose_name=_('Comment Text'))  
    stars = models.CharField(max_length=1, choices=PRODUCT_STARS, verbose_name=_('Stars')) 
    active = models.BooleanField(default=True, verbose_name=_('Active'))  

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))  
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date Modified'))  

    # Manager
    objects = models.Manager()
    active_true = ActiveCommentsManager()

    def __str__(self):
        return self.author.username

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.pk])
