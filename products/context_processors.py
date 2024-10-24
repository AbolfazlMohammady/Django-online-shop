from .models import Product

def product(request):
    return {'product': Product}