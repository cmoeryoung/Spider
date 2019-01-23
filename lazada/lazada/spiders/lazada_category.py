from scrapy import Request,Spider
from urllib.parse import quote
from lazada.items import LazadaItem

class LazadaSpider(Spider):
    name = 'lazada'
    allowed_domains = ['www.lazada.com.my']
    base_url = 'https://www.lazada.com.my'

    def start_requests(self):
        url = 'https://www.lazada.com.my'
        yield Request(url=url,callback=self.parse)

    def parse(self, response):
