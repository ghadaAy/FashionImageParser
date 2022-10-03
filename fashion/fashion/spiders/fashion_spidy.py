from logging import raiseExceptions
from fashion.items import FashionItem
import scrapy
import json
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.pipelines.images import ImagesPipeline

class FashionSpidySpider(scrapy.Spider):
    name = 'fashion_spidy'
    allowed_domains = ['bershka.com']
    start_urls = ['https://www.bershka.com/es/en/women/clothes/jackets-c1010193212.html']
   
    
    def parse(self, response):
        
        try:
            for link in response.xpath('//a[contains(@href, @class)]/@href'):
                if 'clothes' in link.get():
                    yield response.follow(link.get(), callback = self.parse_items)
        except:
            raiseExceptions("Can't connect")

    @staticmethod
    def _string_manoeuvre(string:str):
        return string.replace('\n','').replace(' ','_').replace('___','_').replace('__','_')

    def parse_items(self, response):
        try:
            
            product_name = response.css(".product-title::text").get()
            product_color = response.css(".description::text").get()

            img_url = response.css("img").xpath('@data-original').extract()
            img_names = [self._string_manoeuvre(f"{product_name}_{product_color.split(':')[-1]}_{i}") for i in range(len(img_url))]

            for el, name in zip(img_url,img_names):
                yield {'image_urls': [el],
                        'image_name': name}  
        except:
            pass
