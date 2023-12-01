# Додайте до банкомату меню отримання поточного курсу валют за
# допомогою requests (можна використати відкрите API ПриватБанку)
import requests


def get_exchange_rate():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    print('Current exchange rate:\n'
          f'{"-" * 20}')
    for exchange_rate in response.json():
        print(f'Currency: {exchange_rate["ccy"]}\n'
              f'Base currency: {exchange_rate["base_ccy"]}\n'
              f'Buy: {exchange_rate["buy"]}\n'
              f'Sale: {exchange_rate["sale"]}\n'
              f'{"-" * 20}')
