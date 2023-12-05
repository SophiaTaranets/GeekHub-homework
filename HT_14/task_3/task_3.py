# http://quotes.toscrape.com/ - написати скрейпер для збору всієї
# доступної інформації про записи: цитата, автор, інфа про автора тощо.
# - збирається інформація з 10 сторінок сайту.
# - зберігати зібрані дані у CSV файл
import requests
from bs4 import BeautifulSoup as bs
import csv


BASE_URL = 'http://quotes.toscrape.com/'
FILE_NAME = 'content.csv'


def get_author_information(about_link):
    author_info_url = BASE_URL + about_link
    r = requests.get(author_info_url)
    s = bs(r.text, 'lxml')
    author_info = s.find('div', class_='author-details')

    author_information = {
        'date': author_info.find('span', class_='author-born-date').text,
        'location': author_info.find('span', class_='author-born-location').text,
        'description': author_info.find('div', class_='author-description').text
    }
    return author_information


def scraper():
    content = []
    authors = {}
    current_url = BASE_URL + 'page/1/'
    page_counter = 0

    while True:
        try:
            response = requests.get(current_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page: {e}")
            break

        soup = bs(response.text, 'html.parser')

        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            author_name = quote.a['href'].split('/')[-1]
            if author_name not in authors:
                authors[author_name] = get_author_information(quote.a['href'])

            content.append({'page': str(current_url.split('/')[-2]),
                            'quote': quote.span.text,
                            'author': quote.small.text,
                            'birth_date': authors[author_name]['date'],
                            'location': authors[author_name]['location'],
                            'description': authors[author_name]['description']})

        next_page = soup.find('li', class_='next')
        if not next_page:
            break

        current_url = BASE_URL + next_page.a['href'][1::]
        page_counter += 1

        if page_counter == 10:
            break

    return content


def write_to_file():
    content = scraper()
    with open(FILE_NAME, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['page', 'quote', 'author', 'birth_date', 'location', 'description']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in content:
            print(f'Scraping page: {item["page"]}')
            writer.writerow(item)


write_to_file()
