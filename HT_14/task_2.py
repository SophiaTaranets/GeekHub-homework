#  Створіть програму для отримання курсу валют за певний період.
# - отримати від користувача дату (це може бути як один день так і
# інтервал - початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних
import requests
from datetime import datetime, timedelta


class DateException(Exception):
    pass


class OptionException(Exception):
    pass


class Validation:
    @staticmethod
    def validate_data(value):
        try:
            datetime_obj = datetime.strptime(str(value), '%d.%m.%Y')
        except ValueError:
            raise DateException("Wrong data format")
        return datetime_obj

    @staticmethod
    def check_current_date(date_obj: datetime):
        current_datetime = datetime.now()
        if date_obj > current_datetime:
            raise DateException("Date cannot be in the future")
        if 2008 > date_obj.year:
            raise DateException("Year should be not earlier than 2008")
        return date_obj

    @staticmethod
    def range_date(start: datetime, end: datetime):
        if start > end:
            raise DateException("End date can`t be earlier than start date")
        return start, end


class Currency:
    url = 'https://api.privatbank.ua/p24api/exchange_rates?date='

    def __init__(self, currency, date):
        self.currency = currency
        self.date = date

    def __get_exchange_rate_by_date(self):
        self.url += self.date
        response = requests.get(self.url)
        result_info = {}
        for exchange_rate in response.json()['exchangeRate']:
            if exchange_rate['currency'] == self.currency:
                result_info = exchange_rate
        return result_info

    def __str__(self):
        currency_info = self.__get_exchange_rate_by_date()
        return f'Base currency: {currency_info["baseCurrency"]}\n' \
               f'Currency: {currency_info["currency"]}\n' \
               f'Date: {self.date}\n' \
               f'Buy: {currency_info["purchaseRateNB"]}\n' \
               f'Sale: {currency_info["saleRateNB"]}\n' \
               f'{"-" * 38}'


def currency_menu():
    print('Choose currency:\n'
          '1 - USD\n'
          '2 - EUR\n'
          '3 - PLN\n'
          '4 - CAD\n'
          '5 - SEK\n'
          '6 - GBP\n'
          f'{"-" * 38}')
    currencies = {
        '1': 'USD',
        '2': 'EUR',
        '3': 'PLN',
        '4': 'CAD',
        '5': 'SEK',
        '6': 'GBP'
    }
    currency_option = input('Enter number of the option: ')
    if currency_option not in ('1', '2', '3', '4', '5', '6'):
        raise OptionException('Incorrect option')
    else:
        return currencies[currency_option]


def get_currency_by_range_date():
    try:
        currency = currency_menu()
    except OptionException as e:
        print(f'{"-" * 10} {e} {"-" * 10}')
    else:
        start_date = input('Enter start date in format dd.mm.yyyy (example: 01.12.2023): ')
        end_date = input('Enter end date in format dd.mm.yyyy (example: 01.12.2023): ')
        try:
            v = Validation()
            start_date = v.validate_data(start_date)
            end_date = v.validate_data(end_date)

            start_date = v.range_date(start_date, end_date)[0]
            end_date = v.range_date(start_date, end_date)[1]

            start_date = v.check_current_date(start_date)
            end_date = v.check_current_date(end_date)
        except DateException as error:
            print(f'{"-" * 10} {error} {"-" * 10}')
        else:
            while start_date <= end_date:
                current_date = start_date.strftime('%d.%m.%Y')
                c = Currency(currency, current_date)
                print(c)
                start_date += timedelta(days=1)


def get_currency_by_single_date():
    try:
        currency = currency_menu()
    except OptionException as e:
        print(e)
    else:
        d = input('Enter date in format dd.mm.yyyy (example: 01.12.2023): ')
        try:
            v = Validation()
            d = v.validate_data(d)
            d = v.check_current_date(d)
        except DateException as error:
            print(f'{"-" * 10} {error} {"-" * 10}')
        else:
            d = d.strftime('%d.%m.%Y')
            c = Currency(currency, d)
            print(c)


def main():
    while True:
        print(f'{"-" * 38}\n'
              'Choose option: \n'
              '1 - Get currency by single date\n'
              '2 - Get currency by range of the date\n'
              '0 - Exit')
        user_option = input('Enter your option: ')
        print('-' * 38)
        if user_option == '1':
            get_currency_by_single_date()
        elif user_option == '2':
            get_currency_by_range_date()
        elif user_option == '0':
            if input('Enter "yes" if you really want to exit: ') == 'yes':
                break
            else:
                continue
        else:
            print(f'{"-" * 38} Incorrect option {"-" * 38}')


main()
