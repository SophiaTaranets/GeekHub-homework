from django.urls import path
from .views import (
    get_new_product_id,
    get_all_products,
    product_description,
    add_product_to_cart,
    delete_product_from_cart,
    clear_shopping_cart,
    view_cart,
    increase_cart_item,
    decrease_cart_item,
    filter_product_by_category,
    delete_product,
    edit_product
)

app_name = 'product'
urlpatterns = [
    path('products/', get_all_products, name='products_list'),
    path('product/<int:pid>/', product_description, name='product_description'),
    path('category/<int:category_id>/filter/', filter_product_by_category, name='filter_product_by_category'),
    path('new_id/', get_new_product_id, name='new_product_id'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_product_to_cart, name='add_product_to_cart'),
    path('cart/remove/<int:product_id>/', delete_product_from_cart, name='delete_product_from_cart'),
    path('product/delete/<int:product_id>/', delete_product, name='delete_product'),
    path('product/edit/<int:product_id>/', edit_product, name='edit_product'),
    path('cart/clear/', clear_shopping_cart, name='clear_shopping_cart'),
    path('cart/increase/<int:product_id>/', increase_cart_item, name='increase_cart_item'),
    path('cart/decrease/<int:product_id>/', decrease_cart_item, name='decrease_cart_item')
]
