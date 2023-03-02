import scrapy
from douyu.items import DouyuItem

class DouySpider(scrapy.Spider):
    name = 'douy'
    allowed_domains = ['www.douyu.com']
    start_urls = [f'https://m.douyu.com/api/room/list?page={j}&type=yz'for j in range(1,100)]

    def parse(self, response,**kwargs):
        data_json = response.json()
        """转字典"""
        data = data_json["data"]["list"]
        for i in data:
            item = DouyuItem()
            item["title"] = i['roomName']
            item["url"] = i['avatar']
            item['hn'] = i['hn']
            print(item["title"])
            yield item

