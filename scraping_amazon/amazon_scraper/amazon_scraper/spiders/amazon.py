import scrapy
from ..items import AmazonScraperItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        items = AmazonScraperItem()
        
        product_name = response.css("").extract()
        product_author = response.css("").extract()
        product_price = response.css("").extract()
        product_imagelink = response.css("").extract()
        
        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink
        
        yield items