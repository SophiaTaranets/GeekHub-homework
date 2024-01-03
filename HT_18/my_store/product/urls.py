from django.urls import path
from .views import get_new_product_id, get_all_products, product_description


app_name = 'product'
urlpatterns = [
    path('', get_all_products, name='products_list'),
    path('<int:pid>/', product_description, name='product_description'),
    path('new_id/', get_new_product_id, name='new_product_id'),
]
