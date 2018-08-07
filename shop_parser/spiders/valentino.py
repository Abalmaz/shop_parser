import scrapy
from shop_parser.items import Product


class ShopSpider(scrapy.Spider):
    name = 'valentino'
    start_urls = ['https://www.valentino.com/en-us/women/pret-a-porter'
                  # , 'https://www.valentino.com/en-us/men/apparel'
                  ]

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                                                                  'AppleWebKit/537.36 (KHTML, '
                                                                                  'like Gecko) Chrome/67.0.3396.99 '
                                                                                  'Safari/537.36'})

    def parse(self, response):
        for url in response.xpath('//ul[@id="wrapper-product-lists"]/div[@class="wrapper-shelf"]/'
                                  'li[@class="searchresult__item"]/figure/'
                                  'a[not(contains(@class, "item__wrapperImage"))]'
                                  '/@href').extract():
            yield scrapy.Request(url, callback=self.pars_clother)

    def pars_clother(self, response):
        product = Product()
        product['name'] = response.xpath('//article[@class="item"]/div[contains(@class, "item__info")]/'
                                         'h1/span/text()').extract()
        product['brand'] = 'Valentino'
        product['color'] = response.xpath('//div[@class="item-colorAndSize"]/div[@class="item-colorSelection "]/'
                                          'div/ul/li/div/div/span[@class="colorText"]/text()').extract()
        product['description'] = ''.join(s.extract() for s in response.xpath('//ul[@class="infoAccordion"]/'
                                                                             'li[contains(@class,"infoAccordion__details")]/'
                                                                             'div[@class="infoAccordion__description"]/'
                                                                             'div[@class="editorial"]/p/'
                                                                             'span[@class="value"]/text()'))
        product['currency'] = response.xpath('//div[contains(@class,"item__info")]/div[@class="item-price"]/'
                                             'div/div/span/span[@class="currency"]/text()').extract()
        product['price'] = response.xpath('//div[contains(@class,"item__info")]/div[@class="item-price"]/'
                                          'div/div/span/span[@class="value"]/text()').extract()
        product['size'] = response.xpath('//div[@class="item-colorAndSize"]/div[@class="item-sizeSelection "]/'
                                         'div/ul/li/span[@class="sizeLabel"]/text()').extract()
        product['image'] = response.xpath('//div[contains(@class,"imagesContent")]/div[contains(@class,"mainImage")]/'
                                          'div/ul/li/img/@src').extract()

