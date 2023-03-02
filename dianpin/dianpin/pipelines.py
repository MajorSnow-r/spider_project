# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
from pymongo import MongoClient

"""写入csv文件"""


class DianpinPipeline:

    def open_spider(self, spider):
        with open("360点评.csv", mode="w", encoding="utf-8", newline="") as f:
            self.write = csv.DictWriter(f, fieldnames=['title', 'pingjia', 'pingfen', 'dianpin', 'baoguang', 'name',
                                                       'colour', 'text', 'date'])
            self.write.writeheader()

    def process_item(self, item, spider):
        with open('360点评.csv', mode="a", encoding='utf-8', newline="") as f:
            self.write = csv.DictWriter(f, fieldnames=['title', 'pingjia', 'pingfen', 'dianpin', 'baoguang', 'name',
                                                       'colour',
                                                       'text', 'date'])
            self.write.writerow(item)
        return item


"""写入数据库"""


class mongdbPipeline:

    def open_spider(self, spider):
        self.db = MongoClient()
        """创建数据库"""
        self.dbbase = self.db['dianpin']

    def process_item(self, item, spider):
        """写入数据"""
        self.dbbase.dp.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.db.close()
