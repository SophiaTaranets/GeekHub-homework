from rest_framework import viewsets, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from .models import Product, ProductCategory, ShoppingCart
from .permissions import IsAdminOrIfAuthentificateReadOnly, IsAdminOrIfAuthentificate
from .serializers import ProductSerializer, ScrapingTaskSerializer, ProductCategorySerializer, ShoppingCartSerializer, \
    ShoppingCartListSerializer, ShoppingCartCreateSerializer, ShoppingCartDeleteSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = (IsAdminOrIfAuthentificateReadOnly, )
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = ScrapingTaskSerializer(products_array=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                'success_message': 'Products were added',
                **serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    permission_classes = (IsAdminOrIfAuthentificateReadOnly, )
    serializer_class = ProductCategorySerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "list":
            return ShoppingCartListSerializer
        elif self.action == "create":
            return ShoppingCartCreateSerializer
        elif self.action == "destroy":
            return ShoppingCartDeleteSerializer
        return ShoppingCartSerializer

    def list(self, request, *args, **kwargs):
        queryset = ShoppingCart.objects.all()
        serializer = ShoppingCartListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data['product_id']
        shopping_cart = request.session.get('shopping_cart') or {}

        if str(product_id) in shopping_cart:
            return Response({'error': f'Product with id {product_id} already exists in the cart'},
                            status=status.HTTP_400_BAD_REQUEST)

        shopping_cart[str(product_id)] = 1
        request.session['shopping_cart'] = shopping_cart
        request.session.modified = True

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data['product_id']
        shopping_cart = request.session.get('shopping_cart') or {}

        if str(product_id) in shopping_cart:
            shopping_cart.pop(str(product_id))
            request.session['shopping_cart'] = shopping_cart
            request.session.modified = True
        else:
            return Response({'error': f'No product with id {product_id} in the cart'},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateTokenView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


