import scrapy
from bs4 import BeautifulSoup


class GoogleSpider(scrapy.Spider):
    name = 'google'
    # allowed_domains = ['chrome.google.com']
    BASE_URL = 'https://chrome.google.com/webstore/sitemap'

    def start_requests(self):
        yield scrapy.Request(url=self.BASE_URL, callback=self.parse_map)

    def parse_map(self, response):
        soup = BeautifulSoup(response.body, 'xml')
        for url in soup.select('sitemap > loc'):
            yield scrapy.Request(url=url.text, callback=self.parse_urls)

    def parse_urls(self, response):
        soup = BeautifulSoup(response.body, 'xml')
        for url in soup.select('url > loc'):
            if "/detail" not in url.text:
                continue
            yield scrapy.Request(url=url.text, callback=self.parse_extensions)

    def parse_extensions(self, response, **kwargs):
        id_ = response.css('[property="og:url"]::attr(content)').get().split('/').pop()
        yield {
            'id': f'{id_}',
            'name': response.css('[property="og:title"]::attr(content)').get(),
            'description': response.css('[property="og:description"]::attr(content)').get()
        }
