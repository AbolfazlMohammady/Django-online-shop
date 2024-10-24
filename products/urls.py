from django.urls import path
from . import views


urlpatterns = [
    path('' ,views.ProductListView.as_view(), name='product-list'),
    path('<int:pk>/' ,views.product_detail_view, name='product-detail'),
    path('search/', views.product_search, name='product_search'),
]
