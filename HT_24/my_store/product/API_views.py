from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.settings import api_settings

from .models import Product, ProductCategory, ShoppingCart, ShoppingCartItem
from .permissions import IsAdminOrIfAuthentificate
from .serializers import ProductSerializer, ProductCategorySerializer, ShoppingCartSerializer, \
    ShoppingCartItemSerializer, ShoppingCartListSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ShoppingCartListSerializer
        return ShoppingCartSerializer

    def list(self, request, *args, **kwargs):
        queryset = ShoppingCart.objects.all()
        serializer = ShoppingCartListSerializer(queryset, many=True)
        return Response(serializer.data)

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrIfAuthentificate,)


class ShoppingCartItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer


class CreateTokenView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
