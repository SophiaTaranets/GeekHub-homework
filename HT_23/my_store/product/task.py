from .models import Product
from .models import ProductCategory
from .scraper.sears_api import SearsAPI
from my_store.celery import celery_app


@celery_app.task
def scrape_and_save_product(product_id):
    scraper = SearsAPI(product_id)
    data = scraper.get_product_important_information()
    if data:
        parent_category_name = data.get('category')
        category, category_created = ProductCategory.objects.get_or_create(name=parent_category_name)
        data['category'] = category
        product, product_created = Product.objects.update_or_create(product_id=product_id, defaults=data)
        return f"Product with id {product_id} was {'created' if product_created else 'updated'}"
    else:
        return f"Failed to scrape product with id {product_id}"