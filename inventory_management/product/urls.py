

from django.urls import path
from .views import get_products, get_product_detail, update_product, delete_product

urlpatterns = [
    path('', get_products, name='get-product'),
    path('<int:pk>/', get_product_detail, name='get-product-detail'),
    path('update/<int:pk>/', update_product, name='update-product'),
    path('delete/<int:pk>/', delete_product, name='delete-product'),
]