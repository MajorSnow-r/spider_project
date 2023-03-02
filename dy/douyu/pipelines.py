# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re

import requests
import scrapy
from itemadapter import ItemAdapter
import urllib.request
from scrapy.pipelines.images import ImagesPipeline

class DouyuPipeline:
    def process_item(self, item, spider):

        return item


class DouyuPipeline1(ImagesPipeline):

    def get_media_requests(self, item, info):
        img_url = item["url"]
        yield scrapy.Request(img_url)
    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = item["title"]
        return f'斗鱼/{image_guid}.jpg'