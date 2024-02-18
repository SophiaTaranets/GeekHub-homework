from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from HT_24.my_store.product.models import Product, ProductCategory


class ProductTestCase(TestCase):
    def setUp(self):
       self.client.login(username='user', password='useruser')
       self.product_1 = Product.objects.create(name='product', price=30, brand_name='b-name', product_id='A-test', product_url='test-url', category='test-category')
       product_2 = Product.objects.create(name='product', price=25, brand_name='b-name', product_id='A-test', product_url='test-url', category='test-category')
       product_3 = Product.objects.create(name='product', price=20, brand_name='b-name', product_id='A-test', product_url='test-url', category='test-category')

    def test_product_create(self):
        url = reverse('products_list')
        product_category = ProductCategory.objects.get(name=self.product_1['category'])
        category_id = product_category.id
        self.product_1['category'] = category_id
        response = self.client.post(url, self.product_1)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_person_list_view(self):
        url = reverse('product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['product']), 3)

    def test_get_product_description(self):
        url = reverse('product_description', kwargs={'pk': self.product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_products_view(self):
        url = reverse('products_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        url = reverse('product_description', kwargs={'pk': self.product.id})
        product_category = ProductCategory.objects.get(name=self.product_data['parent_category'])
        category_id = product_category.id
        product_data = self.product_1
        product_data['category'] = category_id
        product_data['name'] = 'product to update'
        response = self.client.put(url, product_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_product(self):
        url = reverse('product_description', kwargs={'pk': self.product.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_product_to_cart(self):
        url = reverse('add_product_to_cart')
        data = {
            'product': self.product.id,
            'amount': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product_from_cart(self):
        url = reverse('delete_product_from_cart')
        product_id = self.product.id
        data = {'product_id': product_id}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        nunber_of_cart_items = len(response.data)
        self.assertEqual(nunber_of_cart_items, 0)
