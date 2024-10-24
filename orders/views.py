from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem


@login_required
def order_created(request):
    cart = Cart(request)
    
    if len(cart) == 0:
        messages.warning(request ,_('you can not proceed to checkout page because your cart is empty.'))
        return redirect('product-list')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_obj = form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order = order_obj,
                    product = product,
                    quantity = item['quantity'],
                    price = product.price, 
                )
            
            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            messages.success(request, _('you order successfully placed.'))

            request.session['order_id'] = order_obj.id
            return redirect('payment-process')
    else:
        form = OrderForm()


    return render(request, 'orders/order_create.html', context={
        'form': form
    })
