from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import IDForm, ProductForm
from .models import ScrapingTask, Product, ShoppingCart, ShoppingCartItem, ProductCategory
from .scraper.sears_api import SearsAPI
from .task import scrape_and_save_product

def get_new_product_id(request):
    if request.method == "POST":
        form = IDForm(request.POST)
        if form.is_valid():
            form.save()
            received_ids = ScrapingTask.objects.last().ids
            new_products_ids = received_ids.split('\n')
            for product_id in new_products_ids:
                scrape_and_save_product.delay(product_id)
    else:
        form = IDForm()
    return render(request, 'product/add_new_product_form.html', context={'form': form})


def new_product(id_product):
    product_information = SearsAPI(id_product)
    product_information = product_information.get_product_important_information()
    if product_information:
        category, created = ProductCategory.objects.get_or_create(name=product_information['category'])
        Product.objects.update_or_create(
            product_id=product_information['product_id'],
            defaults={'name': product_information['name'],
                      'category': category,
                      'price': product_information['price'],
                      'brand_name': product_information['brand_name'],
                      'product_url': product_information['url']})


def get_all_products(request, category_id=None):
    categories = ProductCategory.objects.all().distinct()
    all_products = Product.objects.all()

    if category_id:
        category = get_object_or_404(ProductCategory, id=category_id)
        all_products = all_products.filter(category=category)

    context = {'categories': categories, 'all_products': all_products}
    return render(request, 'product/products_information.html', context)


def product_description(request, pid):
    product = get_object_or_404(Product, id=pid)
    return render(request, 'product/product_description.html', context={'product': product})


def view_cart(request):
    shopping_cart, created = ShoppingCart.objects.get_or_create()
    shopping_cart_items = ShoppingCartItem.objects.filter(shopping_cart=shopping_cart)
    return render(request, 'product/shopping_cart.html', context={'cart_items': shopping_cart_items})


def add_product_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart, created = ShoppingCart.objects.get_or_create()
    cart_item, item_created = ShoppingCartItem.objects.get_or_create(shopping_cart=cart, product=product)

    if not item_created:
        cart_item.amount += 1
        cart_item.save()
    all_products = Product.objects.all()

    return render(request, 'product/products_information.html', context={'all_products': all_products})


def increase_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    shopping_cart = ShoppingCart.objects.get()
    cart_item, item_created = ShoppingCartItem.objects.get_or_create(shopping_cart=shopping_cart, product=product)
    cart_item.amount += 1
    cart_item.save()

    return render(request, 'product/shopping_cart.html',
                  context={'cart_items': ShoppingCartItem.objects.filter(shopping_cart=shopping_cart)})


def decrease_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    shopping_cart = ShoppingCart.objects.get()
    cart_item, item_created = ShoppingCartItem.objects.get_or_create(shopping_cart=shopping_cart, product=product)

    if cart_item.amount > 1:
        cart_item.amount -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return render(request, 'product/shopping_cart.html',
                  context={'cart_items': ShoppingCartItem.objects.filter(shopping_cart=shopping_cart)})


def delete_product_from_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    shopping_cart = ShoppingCart.objects.get()

    try:
        cart_item = ShoppingCartItem.objects.get(shopping_cart=shopping_cart, product=product)
        cart_item.delete()

    except Exception:
        pass
    return redirect('product:products_list')
    # return render(request, 'product/products_information.html',
    #               context={'cart_items': ShoppingCartItem.objects.filter(shopping_cart=shopping_cart)})


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if not request.user.is_superuser:
        messages.error(request, 'You can`t delete products')
        return redirect('product:products_list')
    try:
        product.delete()
    except Exception:
        pass
    return redirect('product:products_list')
    # return render(request, 'product/products_information.html')


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = ProductCategory.objects.all().distinct()
    if not request.user.is_superuser:
        messages.error(request, 'You can\'t edit products')
        return redirect('product:products_list')

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            print("Form data:", form.cleaned_data)
            form.save()
            return redirect('product:products_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product/edit_product.html', {'form': form, 'product': product,'categories': categories})


def clear_shopping_cart(request):
    shopping_cart = ShoppingCart.objects.get()
    shopping_cart_items = ShoppingCartItem.objects.all()
    try:
        for item in shopping_cart_items:
            item.delete()
    except Exception:
        pass
    return render(request, 'product/shopping_cart.html',
                  context={'cart_items': ShoppingCartItem.objects.filter(shopping_cart=shopping_cart)})


def filter_product_by_category(request, category_id):
    category = get_object_or_404(ProductCategory, id=category_id)
    categories = ProductCategory.objects.all().distinct()
    filtered_products = Product.objects.filter(category_id=category)
    return render(request, 'product/filtered_products.html', context={'filtered_products': filtered_products,
                                                                      'category': category,
                                                                      'categories': categories})
