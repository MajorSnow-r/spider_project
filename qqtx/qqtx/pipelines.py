# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from urllib.request import urlretrieve
import os


class QqtnPipeline:
    """创建文件夹"""
    wjian = os.getcwd() + "\\情侣头像\\"
    if not os.path.exists(wjian):
        os.makedirs(wjian)
    sum = 0

    def process_item(self, item, spider):
        """保存数据"""
        urlretrieve(item['src'], self.wjian + item['title'] + str(self.sum) + '.jpg')
        self.sum += 1
        return item
