from django.urls import include, path
from rest_framework import routers
from . import API_views
from .API_views import ShoppingCartItemViewSet, CreateTokenView

app_name = 'api'
router = routers.DefaultRouter()
router.register('products', API_views.ProductViewSet)
router.register('categories', API_views.ProductCategoryViewSet)
router.register('shopping_cart', API_views.ShoppingCartViewSet, basename='shopping_cart')
router.register('shopping_cart_items', ShoppingCartItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', CreateTokenView.as_view(), name="token")
]

urlpatterns += router.urls