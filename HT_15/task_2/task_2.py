# Викорисовуючи requests, заходите на ось цей сайт "https://www.expireddomains.net/deleted-domains/"
# (з ним будьте обережні), вибираєте будь-яку на ваш вибір доменну зону і парсите список
# доменів - їх там буде десятки тисяч (звичайно ураховуючи пагінацію).
# Всі отримані значення зберігти в CSV файл.
import csv
import random

import requests
from bs4 import BeautifulSoup as bs
from random import choice
import time

BASE_URL = "https://www.expireddomains.net"
TLD_URL = 'tld'
DOMAIN_NAME = '.com'
SESSION = requests.Session()


def generate_headers():
    random_user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 '
        'Safari/537.36',

        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59 '
        'Safari/537.36',

        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    ]

    headers = {
        'User-Agent': choice(random_user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Sec-Ch-UA': '"Google Chrome";v="107","Chromium";v="107","Not A;Brand";v="24"',
        'Sec-Ch-UA-Mobile': '?0',
        'Sec-Ch-UA-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1'
    }

    return headers


def create_tlds_response():
    # get response to tlds: list with domains names
    url = f'{BASE_URL}/{TLD_URL}s/'
    response = SESSION.get(url, headers=generate_headers())
    return response


def get_domain_url():
    # create url for current domain
    response = create_tlds_response()
    soup = bs(response.text, 'lxml')
    domain_names = soup.find_all('strong')
    url = ''
    for domain_name in domain_names:
        if domain_name and domain_name.find('a'):
            if domain_name.find('a').text == DOMAIN_NAME:
                url += f'{BASE_URL}/{TLD_URL}/{DOMAIN_NAME[1::]}/'
    return url


def get_domains_list_url():
    # create url for list of current domain
    url = get_domain_url()
    response = SESSION.get(url, headers=generate_headers())
    soup = bs(response.text, 'lxml')
    pending = soup.find('a', title='Pending Delete Domains')
    base_domains_url = f'{BASE_URL}{pending["href"]}'.split('/')
    base_domains_url.pop()
    return '/'.join(base_domains_url) + '/'


def parse_headers(url):
    # url = get_domains_list_url()
    response = SESSION.get(url, headers=generate_headers())
    soup = bs(response.text, 'lxml')
    headers = soup.find_all('th')
    headers_title = [title.a.text for title in headers]
    return headers_title


def parse_rows(url):
    # url = get_domains_list_url()
    response = SESSION.get(url, headers=generate_headers())
    soup = bs(response.text, 'lxml')
    all_rows = soup.find('tbody').find_all('tr')
    rows_info = []
    for row in all_rows:
        temp_row = row.find_all('td')
        # print(temp_row)
        current_row = []
        for item in temp_row:

            if item.a:
                current_row.append(item.a.text)

            else:
                current_row.append(item.text)
        rows_info.append(current_row)
    return rows_info


def get_all_domains():
    all_domains = []
    start_url = get_domains_list_url()
    headers = parse_headers(start_url)
    rows = parse_rows(start_url)
    all_domains.append(headers)
    all_domains.append(rows)
    for page in range(25, 325, 25):
        time.sleep(random.randrange(10, 25))
        next_page = f'{start_url}?start={page}#listing'
        next_rows = parse_rows(next_page)
        all_domains.append(next_rows)
    return all_domains


def write_to_file():
    with open('domains_data.csv', 'w') as file:
        writer = csv.writer(file)
        domains = get_all_domains()
        for header in domains:
            writer.writerow(header)
            break
        for row in domains[1::]:
            for domain in row:
                writer.writerow(domain)


write_to_file()
