from django.shortcuts import render, get_object_or_404
from .forms import IDForm
from .models import ScrapingTask, Product
from .scraper.sears_api import SearsAPI


def get_new_product_id(request):
    if request.method == "POST":
        form = IDForm(request.POST)
        if form.is_valid():
            form.save()
            received_ids = (ScrapingTask.objects.all().last()).ids
            new_products_ids = received_ids.split('\n')
            for product_id in new_products_ids:
                new_product(product_id)
    else:
        form = IDForm()
    return render(request, 'product/add_new_product_form.html', context={'form': form})


def new_product(id_product):
    product_information = SearsAPI(id_product) # 108305436
    product_information = product_information.get_product_important_information()
    if product_information:
        Product.objects.update_or_create(
            product_id=product_information['product_id'],
            defaults={'name': product_information['name'],
                      'price': product_information['price'],
                      'brand_name': product_information['brand_name'],
                      'product_url': product_information['url']})


def get_all_products(request):
    all_products = Product.objects.all()
    return render(request, 'product/products_information.html', context={'all_products': all_products})


def product_description(request, pid):
    product = get_object_or_404(Product, id=pid)
    return render(request, 'product/product_description.html', context={'product': product})
