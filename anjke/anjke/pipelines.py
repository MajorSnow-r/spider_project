# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
from pymongo import MongoClient


class AnjkePipeline:
    
    def open_spider(self,spider):
        mongo = MongoClient()
        self.db = mongo["yundata"]["data"]

    def process_item(self, item, spider):
        self.db.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        pass
