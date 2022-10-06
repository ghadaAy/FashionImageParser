# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from unicodedata import category
import scrapy
from scrapy import Field


class FashionItem(scrapy.Item):
    image_name = Field()
    img_url = Field()

class ImageItem(scrapy.Item):
    image_urls = Field()
    images = Field()
