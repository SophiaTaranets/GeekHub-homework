from django.core.management import BaseCommand
from HT_22.my_store.product.models import Product
from HT_22.my_store.product.scraper import sears_api


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('ids', nargs="+", type=str)

    def handle(self, *args, **options):
        split_ids = options['ids'][0].split(',')
        exist_ids = []
        print(f'Added to the queue {len(split_ids)}')
        for product_id in split_ids:
            product = sears_api.get_parsed_data(product_id)
            if product is not None:
                exist_ids.append(product_id)
                self.update_product(product_id, product)
        if exist_ids:
            print(f'Finished data update {len(exist_ids)} products with {exist_ids}')
        else:
            print(f'Finished data update product_id: {split_ids} does not exist')

    def update_product(self, product_id, product_data):
        """
        Renew product data
        """
        Product.objects.update_or_create(product_id=product_id, defaults=product_data)
        print(f"Successfully request. Updated product with id{product_id}")
