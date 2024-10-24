from django.urls import path
from . import views


urlpatterns = [
    path('' ,views.cart_detail_view, name='cart-detail'),
    path('clear/' ,views.clear_all_cart, name='cart-clear'),
    path('add/<int:pk>' ,views.add_to_cart_view, name='add-cart'),
    path('remove/<int:pk>' ,views.remove_from_view, name='remove-cart'),
]
