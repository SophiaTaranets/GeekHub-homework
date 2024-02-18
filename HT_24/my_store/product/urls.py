from django.urls import path
from .views import get_new_product_id, get_all_products, product_description, add_product_to_cart, \
    delete_product_from_cart, clear_shopping_cart, view_cart, increase_cart_item, decrease_cart_item, \
    filter_product_by_category, delete_product, edit_product

app_name = 'product'
urlpatterns = [
    path('', get_all_products, name='products_list'),
    path('<int:pid>/', product_description, name='product_description'),
    path('category/<int:category_id>/', filter_product_by_category, name='filter_product_by_category'),
    path('new_id/', get_new_product_id, name='new_product_id'),
    path('view_cart', view_cart, name='view_cart'),
    path('add_product_to_cart/<int:product_id>/', add_product_to_cart, name='add_product_to_cart'),
    path('delete_product_from_cart/<int:product_id>/', delete_product_from_cart, name='delete_product_from_cart'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('clear_shopping_cart', clear_shopping_cart, name='clear_shopping_cart'),
    path('increase_cart_item/<int:product_id>/', increase_cart_item, name='increase_cart_item'),
    path('decrease_cart_item/<int:product_id>/', decrease_cart_item, name='decrease_cart_item')
]
