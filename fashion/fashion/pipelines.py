# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from urllib.request import Request
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class FashionPipeline(ImagesPipeline):
    pass

    def get_media_requests(self,item,info=None):
        for image_url in item['image_urls']:
            yield scrapy.Request(url=image_url,meta= {'image_name': item['image_name'], 'category':item['category']} )

    def file_path(self, request, response=None, info=None,item=None):
        return request.meta['image_name']+'.jpg'