# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy import Field


class FashionItem(scrapy.Item):
    image_name = Field()
    img_url = scrapy.Field()
# ScrapingList Residential & Yield Estate for sale


class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()