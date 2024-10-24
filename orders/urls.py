from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.order_created, name='order_create')
]
