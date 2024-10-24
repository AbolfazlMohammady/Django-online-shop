from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model= OrderItem
    fields= ('order', 'product', 'quantity', 'price', )
    extra= 0


@admin.register(Order)
class OrdertAdmin(admin.ModelAdmin):
    list_display= ('user', 'first_name', 'last_name', 'phone' ,'datetime_created' ,'is_paid',)

    inlines= [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''Admin View for OrderItem'''

    list_display = ('order', 'product', 'quantity', 'price', )
    list_filter = ('product',)
    search_fields = ('product',)

