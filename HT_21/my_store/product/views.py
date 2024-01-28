from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import IDForm
from .scraper.scraper_subprocess import run_scraper_in_subprocess
from .scraper.sears_api import SearsAPI
from .serializers import ProductSerializer, ShoppingCartItemSerializer, ProductCategorySerializer
from .models import Product, ShoppingCart, ShoppingCartItem, ProductCategory, ScrapingTask


@api_view(['POST'])
def get_new_product_id(request):
    if request.method == "POST":
        form = IDForm(request.POST)
        if form.is_valid():
            form.save()
            received_ids = ScrapingTask.objects.last().ids
            new_products_ids = received_ids.split('\n')
            for product_id in new_products_ids:
                new_product(product_id)
            return Response({"message": "New products added successfully."})
    else:
        form = IDForm()
    return Response({"message": "New products added successfully."})


def new_product(id_product):
    product_information = SearsAPI(id_product)
    product_information = product_information.get_product_important_information()

    if product_information:
        # Створюємо серіалізатор для категорії
        category_serializer = ProductCategorySerializer(data={'name': product_information['category']})
        category_serializer.is_valid(raise_exception=True)
        category = category_serializer.save()

        # Створюємо серіалізатор для продукту
        product_serializer = ProductSerializer(data={
            'product_id': product_information['product_id'],
            'name': product_information['name'],
            'category': category.id,
            'price': product_information['price'],
            'brand_name': product_information['brand_name'],
            'product_url': product_information['url']
        })
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()

        run_scraper_in_subprocess(product_serializer.data)


@api_view(['GET'])
def get_all_products(request, category_id=None):
    categories = ProductCategory.objects.all().distinct()
    all_products = Product.objects.all()

    if category_id:
        category = get_object_or_404(ProductCategory, id=category_id)
        all_products = all_products.filter(category=category)

    serializer = ProductSerializer(all_products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_description(request, pid):
    product = get_object_or_404(Product, id=pid)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def view_cart(request):
    shopping_cart, created = ShoppingCart.objects.get_or_create()
    shopping_cart_items = ShoppingCartItem.objects.filter(shopping_cart=shopping_cart)
    serializer = ShoppingCartItemSerializer(shopping_cart_items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_product_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = ShoppingCart.objects.get_or_create()
    cart_item, item_created = ShoppingCartItem.objects.get_or_create(shopping_cart=cart, product=product)

    if not item_created:
        cart_item.amount += 1
        cart_item.save()

    serializer = ProductSerializer(Product.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def increase_cart_item(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    shopping_cart = ShoppingCart.objects.get()
    cart_item, item_created = ShoppingCartItem.objects.get_or_create(shopping_cart=shopping_cart, product=product)
    cart_item.amount += 1
    cart_item.save()

    serializer = ShoppingCartItemSerializer(ShoppingCartItem.objects.filter(shopping_cart=shopping_cart), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def decrease_cart_item(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    shopping_cart = ShoppingCart.objects.get()
    cart_item, item_created = ShoppingCartItem.objects.get_or_create(shopping_cart=shopping_cart, product=product)

    if cart_item.amount > 1:
        cart_item.amount -= 1
        cart_item.save()
    else:
        cart_item.delete()

    serializer = ShoppingCartItemSerializer(ShoppingCartItem.objects.filter(shopping_cart=shopping_cart), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def delete_product_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    shopping_cart = ShoppingCart.objects.get()

    try:
        cart_item = ShoppingCartItem.objects.get(shopping_cart=shopping_cart, product=product)
        cart_item.delete()
    except ShoppingCartItem.DoesNotExist:
        pass

    serializer = ProductSerializer(Product.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        return Response({"message": "You can't delete products."}, status=status.HTTP_403_FORBIDDEN)

    try:
        product.delete()
        return Response({"message": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response({"message": "Error deleting product."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = ProductCategory.objects.all().distinct()
    if not request.user.is_superuser:
        return Response({"message": "You can't edit products."}, status=403)

    if request.method == 'POST':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        serializer = ProductSerializer(product)

    return Response(serializer.data)


@api_view(['POST'])
def clear_shopping_cart(request):
    shopping_cart = ShoppingCart.objects.get()
    shopping_cart_items = ShoppingCartItem.objects.all()

    try:
        for item in shopping_cart_items:
            item.delete()
    except Exception:
        pass

    serializer = ShoppingCartItemSerializer(ShoppingCartItem.objects.filter(shopping_cart=shopping_cart), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def filter_product_by_category(request, category_id):
    category = get_object_or_404(ProductCategory, id=category_id)
    categories = ProductCategory.objects.all().distinct()
    filtered_products = Product.objects.filter(category_id=category)
    serializer = ProductSerializer(filtered_products, many=True)
    return Response(serializer.data)
