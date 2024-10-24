from django.contrib import admin
from django.urls import path, include
from  django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('orders.urls')),
    path('payment/', include('payment.urls')),
    path('', include('bookmark.urls')),

     #rosetta
    path('rosetta/', include('rosetta.urls')),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
