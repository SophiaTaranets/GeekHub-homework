import requests
from random import choice
import csv


class SearsCategoryAPI:
    SESSION = requests.session()
    BASE_URL = 'https://www.sears.com'

    def __init__(self, category_id):
        self.category_id = category_id

    @staticmethod
    def generate_user_agent():
        random_user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 '
            'Safari/537.36',

            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59 '
            'Safari/537.36',

            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ]

        return choice(random_user_agents)

    def get_category(self):
        headers = {"Authorization": "SEARS", "User-Agent": self.generate_user_agent()}
        params = {
            'searchType': 'category',
            'catalogId': 12605,
            'store': 'Sears',
            'storeId': 10153,
            'catGroupId': self.category_id
        }

        file_name = '/api/sal/v3/products/search'
        url_category = self.BASE_URL + file_name
        response = requests.get(url_category, headers=headers, params=params)
        return response.json()

    def get_products(self):
        data = self.get_category()
        products_full_data = data['items']
        products = []
        for product in products_full_data:
            products.append(
                {'id': product['id'],
                 'category': product['category'],
                 'brandName': product['brandName'],
                 'name': product['name'],
                 'price': product['price']['messageTags']['finalPrice'],
                 'rating': product['additionalAttributes']['rating']
                 }
            )

        return products

    def write_to_file(self):
        with open(f'{self.category_id}_products.csv', 'w') as file:
            headers = ['id', 'category', 'brandName', 'name', 'price', 'rating']
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

            products = self.get_products()
            for product in products:
                writer.writerow(product)
