from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product, Wishlist

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('product-list')  # صفحه‌ی محصولات

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = get_object_or_404(Wishlist, user=request.user, product=product)
    wishlist_item.delete()
    return redirect('product-list')



@login_required
def wishlist(request):
    wishlisted_products = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlisted_products': wishlisted_products})
