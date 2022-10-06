from logging import raiseExceptions
import scrapy
import os

class FashionSpidySpider(scrapy.Spider):
    name = 'fashion_spidy'
    allowed_domains = ['bershka.com']
    start_urls = ['https://www.bershka.com/es/en/h-woman.html']
    bershka_categories = ['/clothes/','/shoes/','/accessories/']
    base_url = 'https://www.bershka.com/'

    @staticmethod
    def test_string_list_intersection(test_list:list, s:str)->bool:
        """
        Test if an element from list exists insite a string s
        """
        for el in test_list:
            if el in s:
                return True
        return False

    def parse(self,response):
        try:
            links = response.css('.sub-menu-item a').xpath('@href').extract()
            for link in links:
                if link.startswith('/es') and self.test_string_list_intersection(self.bershka_categories, str(link)):
                    link = os.path.join(self.base_url,link)
                    yield response.follow(link, callback = self.parse_one_link)
        except:
            raiseExceptions("problem with response")

    def parse_one_link(self, response):
        pages_links = response.css("a").xpath("@href").extract()
        for link in pages_links:
            try:
                if link.startswith('https') and self.test_string_list_intersection(self.bershka_categories, str(link)):
                    yield response.follow(link, callback = self.parse_items)
            except:
                raiseExceptions("problem with response in category")

    @staticmethod
    def _string_manoeuvre(string:str):
        return string.replace('\n','').replace(' ','_').replace('___','_').replace('__','_')

    def parse_items(self, response):
        try:
            product_name = response.css(".product-title::text").get()
            product_color = response.css(".description::text").get()
            img_url = response.css("img").xpath('@data-original').extract()
            img_name_from_url = response.css("img").xpath('@alt').extract()
            img_names = [self._string_manoeuvre(f"{product_name}_{product_color.split(':')[-1]}_{i}") for i in range(len(img_url))]
            
            for url, name,name_url  in zip(img_url, img_names, img_name_from_url):
                if product_name in name_url:
                    yield {'image_urls': [url],
                            'image_name': name}  
        except:
            raiseExceptions("Error in response for items")

