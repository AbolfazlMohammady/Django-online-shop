from django.urls import path
from . import views


urlpatterns = [
    path('process', views.payment_process, name= 'payment-process'),
]
