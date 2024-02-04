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
    permission_classes = (IsAdminOrIfAuthentificate,)

    def get_serializer_class(self):
        if self.action == "list":
            return ShoppingCartListSerializer
        return ShoppingCartSerializer

    def list(self, request, *args, **kwargs):
        queryset = ShoppingCart.objects.all()
        serializer = ShoppingCartListSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = ShoppingCartCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.session.modified = True

        product_id = serializer.validated_data['product_id']
        shopping_cart = request.session.get('shopping_cart') or {}
        if str(product_id) in shopping_cart:
            return Response({'error': f'Exist'},
                            status=status.HTTP_400_BAD_REQUEST)
        shopping_cart[str(product_id)] = 1
        request.session['shopping_cart'] = shopping_cart
        serializer = ShoppingCartViewSet.list(request)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request):
        if request.data:
            serializer = ShoppingCartDeleteSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            product_id = serializer.validated_data['product_id']

            shopping_cart = request.session.get('shopping_cart') or {}
            if str(product_id) in shopping_cart:
                shopping_cart.pop(str(product_id))
                request.session['cart'] = shopping_cart
                request.session.modified = True
            else:
                return Response({'error': f'No product with{product_id}'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            cart = request.session.get('cart') or {}
            if cart:
                cart.clear()
                request.session['cart'] = cart
                request.session.modified = True
            else:
                return Response({'error': 'Cart is empty'},
                                status=status.HTTP_400_BAD_REQUEST)

        serializer = ShoppingCartViewSet.list(request)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateTokenView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


