from logging import raiseExceptions
import scrapy


class FashionSpidySpider(scrapy.Spider):
    name = 'fashion_spidy'
    allowed_domains = ['bershka.com']
    start_urls = ['https://www.bershka.com/us/h-woman.html']
   
    
    def parse(self, response):
        try:
            for link in response.css(".gender-wrapper").css("a").xpath("@href").extract():
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
            img_name_from_url = response.css("img").xpath('@alt').extract()
            img_names = [self._string_manoeuvre(f"{product_name}_{product_color.split(':')[-1]}_{i}") for i in range(len(img_url))]
            
            for url, name,name_url  in zip(img_url, img_names, img_name_from_url):
                if product_name in name_url:
                    yield {'image_urls': [url],
                            'image_name': name}  
        except:
            pass

##response.css(".gender-wrapper").css("a").xpath("@href").extract()