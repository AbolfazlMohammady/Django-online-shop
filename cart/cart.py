from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from products.models import Product  

class Cart:  
    def __init__(self, request):  
        """  
        Create to cart for user anonymous and register  
        """  
        self.request = request  
        self.session = request.session  

        cart = self.session.get('cart')        

        if not cart:  
            cart = self.session['cart'] = {}  

        self.cart = cart  


    def add(self, product, quantity=1, replace= False):  
        """  
        add product and quantity to cart  
        """  
        product_id = str(product.id)  

        if product_id not in self.cart:  
            self.cart[product_id] = {'quantity': 0}  

        if replace:  
            self.cart[product_id]['quantity'] = quantity 
        else:
            self.cart[product_id]['quantity'] += quantity 
        messages.success(self.request, _('Product Successfully added to cart'))

        self.save()  



    def remove(self, product):  
        product_id = str(product.id)  

        if product_id in self.cart:  
            del self.cart[product_id]  
            messages.success(self.request, _('Product Successfully removed from cart'))

            self.save()  


    def save(self):  
        self.session.modified = True  



    def __iter__(self):   
        product_ids = self.cart.keys()  
        products = Product.objects.filter(id__in=product_ids)  

        for product in products:  
            self.cart[str(product.id)]['product_obj'] = product  

        for item in self.cart.values(): 
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item  
            


    def __len__(self):  
        return len(self.cart.keys())  



    def clear(self):  
        del self.session['cart']  
        self.save()  


    def get_total_price(self):  
        product_ids = self.cart.keys()  
        products = Product.objects.filter(id__in=product_ids)  

        return sum(product.price * self.cart[str(product.id)]['quantity'] for product in products)