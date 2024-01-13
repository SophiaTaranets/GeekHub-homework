import requests
from random import choice


class SearsAPI:
    BASE_URL = 'https://www.sears.com'

    def __init__(self, product_id):
        self.product_id = product_id

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

    def get_product_full_data(self):
        headers = {"Authorization": "SEARS", "User-Agent": self.generate_user_agent()}
        params = {
            'storeName': 'Sears',
            'memberStatus': 'G',
            'zipCode': 10101
        }

        file_name = '/api/sal/v3/products/details/'
        full_product_id = 'A' + self.product_id
        url_category = self.BASE_URL + file_name + full_product_id
        response = requests.get(url_category, headers=headers, params=params)
        return response.json()

    def get_product_important_information(self):
        try:
            data = self.get_product_full_data()
            product_full_info = data['productDetail']['softhardProductdetails'][0]
            product = {'product_id': product_full_info['identity']['sSin'],
                       'category': product_full_info['hierarchies']['specificHierarchy'][1]['name'],
                       'brand_name': product_full_info['brandName'],
                       'name': product_full_info['descriptionName'],
                       'price': product_full_info['price']['finalPrice'],
                       'url': self.BASE_URL + product_full_info['seoUrl']}
        except:
            return False
        else:
            return product


if __name__ == '__main__':
    # product_item = SearsAPI('058982221')
    product_item = SearsAPI('109708650')
    # print(product_item.get_product_full_data())
    print(product_item.get_product_important_information())
