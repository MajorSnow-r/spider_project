# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class WyzpPipeline:

    def open_spider(self, spider):
        with open("网易招聘.csv", mode="w", encoding='utf-8', newline="") as f:
            self.writ = csv.DictWriter(f, fieldnames=['title', "bumen", "zhice", "xli", "rshu", "dizhi", "jingyan",
                                                 "ganw_miaoshu", "gangw_zhize"])
            self.writ.writeheader()

    def process_item(self, item, spider):
        with open("网易招聘.csv", mode="a", encoding='utf-8', newline="") as f:
            self.writ = csv.DictWriter(f, fieldnames=['title', "bumen", "zhice", "xli", "rshu", "dizhi", "jingyan",
                                                      "ganw_miaoshu", "gangw_zhize"])
            self.writ.writerow(item)
        return item
