from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


from products.models import Product

from .cart import Cart
from .forms import AddToCartProductForm



def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_quantity']= AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, 'cart/cart.html',{
        'cart': cart,
    })


@require_POST
def add_to_cart_view(request, pk):
    cart = Cart(request)


    product= get_object_or_404(Product, pk=pk)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']

        cart.add(product, quantity, replace=cleaned_data['inplace'])

        return redirect(reverse('product-list'))
    

    
def remove_from_view(request, pk):
    cart= Cart(request)

    product= get_object_or_404(Product, pk=pk)
    cart.remove(product)
    
    return redirect('cart-detail')


def clear_all_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, _('All product sucsssefully  removedfrom your cart'))
    else:
        messages.warning(request, _('your cart is already empty'))
        
    return redirect(reverse('product-list'))


    




