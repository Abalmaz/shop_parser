import scrapy


class ShopSpider(scrapy.Spider):
    name = 'valentino'
    start_urls = ['https://www.valentino.com/en-us/women/pret-a-porter', 'https://www.valentino.com/en-us/men/apparel']

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                                                                  'AppleWebKit/537.36 (KHTML, '
                                                                                  'like Gecko) Chrome/67.0.3396.99 '
                                                                                  'Safari/537.36'})

    def parse(self, response):
        for url in response.xpath('//div[@class="wrapper-shelf"]/li[@class="searchresult__item"]/a/@href').extract():
            yield scrapy.Request(url, callback=self.pars_clother)

    def pars_clother(self, response):
        pass
