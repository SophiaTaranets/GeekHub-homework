# http://quotes.toscrape.com/ - написати скрейпер для збору всієї
# доступної інформації про записи: цитата, автор, інфа про автора тощо.
# - збирається інформація з 10 сторінок сайту.
# - зберігати зібрані дані у CSV файл
import requests
from bs4 import BeautifulSoup as bs
import csv


BASE_URL = 'http://quotes.toscrape.com/'
FILE_NAME = 'content.csv'


def pagination(page_number):
    return BASE_URL + f'page/{page_number}/'


def scraper():
    content = []
    for i in range(1, 11):
        current_url = pagination(i)
        response = requests.get(current_url)
        soup = bs(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        for quote in quotes:
            author_info_url = BASE_URL + quote.a['href']

            r = requests.get(author_info_url)
            s = bs(r.text, 'lxml')

            author_info = s.find('div', class_='author-details')
            date = author_info.find('span', class_='author-born-date')
            location = author_info.find('span', class_='author-born-location')
            description = author_info.find('div', class_='author-description')

            content.append({'page': str(i),
                            'quote': quote.span.text,
                            'author': quote.small.text,
                            'birth_date': date.text,
                            'location': location.text,
                            'description': description.text})
    return content


def add_to_file():
    content = scraper()
    with open(FILE_NAME, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['page', 'quote', 'author', 'birth_date', 'location', 'description']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in content:
            writer.writerow(item)


add_to_file()
