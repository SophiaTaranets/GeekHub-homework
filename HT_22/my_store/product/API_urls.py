from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views
from . import API_views
from .API_views import CreateTokenView

app_name = 'api'
router = routers.DefaultRouter()
router.register('products', API_views.ProductViewSet)
router.register('categories', API_views.ProductCategoryViewSet)
router.register('shopping_cart', API_views.ShoppingCartViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token),
    # path('login/', CreateTokenView.as_view(), name="token"),

]

urlpatterns += router.urls