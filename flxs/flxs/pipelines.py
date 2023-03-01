# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
import os
from pymongo import MongoClient
"""写入text"""
class FlxsPipeline:

    def process_item(self, item, spider):
        """去除标题中的特殊字符"""
        title = re.sub(r'[\\\/\:\*\？\"\<\>\|\：\,\( \)\.\  \！ \、\，\。\【\：\,\']', "_", item["title"])
        """去除二级标题中的特殊字符"""
        chapter_title = re.sub(r'[\\\/\:\*\？\"\<\>\|\：\,\( \)\'\.\  \！\、\，\。\【\：\..]', "_", item["titles"])
        """地址拼接,从当前地址继续往后面进行拼接"""
        file_path = os.path.join(os.getcwd(), '飞卢小说', title, f'{chapter_title}.txt')
        """dirname返回文件路径,这个的意思就是返回拼接好的文件路径,并且创建出来文件夹"""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directories recursively if they don't exist
        """打开文件夹并且写入内容"""
        with open(file=file_path, mode="a", encoding="utf-8") as f:
            f.write(item["texts"])
        return item



"""写入数据库"""
class MongdbPipeline:

    def open_spider(self,spider):
        self.db = MongoClient()
        self.dbbase = self.db['flxs']

    def process_item(self,item,spider):
        """去除标题中的特殊字符"""
        item['title'] = re.sub(r'[\\\/\:\*\？\"\<\>\|\：\,\( \)\.\  \！ \、\，\。\【\：\,\']', "_", item["title"])
        """去除二级标题中的特殊字符"""
        item['titles'] = re.sub(r'[\\\/\:\*\？\"\<\>\|\：\,\( \)\'\.\  \！\、\，\。\【\：\..]', "_", item["titles"])
        self.dbbase.fl.insert_one(dict(item))
        return item

    def close_spider(self,spider):
        self.db.close()