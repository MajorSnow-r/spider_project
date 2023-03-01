import scrapy
from flxs.items import FlxsItem
from copy import deepcopy
from scrapy_redis.spiders import RedisSpider


class FlSpider(RedisSpider):
    name = 'fl'
    # allowed_domains = ['b.faloo.com']
    # start_urls = ['https://b.faloo.com/y_0_1.html']
    redis_key = 'key'

    """解析首页"""
    def parse(self, response, **kwargs):
        div = response.xpath('//div[@class="TwoBox02_02"]/div[@class="TwoBox02_03"]')
        for i in div:
            item = FlxsItem()
            item['title'] = i.xpath('./a/@title').get()
            href = 'https:' + i.xpath('./a/@href').get()
            yield scrapy.Request(
                url=href,
                callback=self.jiexi,
                meta={"item": deepcopy(item)}
            )

    """解析详情界面"""
    def jiexi(self, response, **kwargs):
        item = response.meta['item']
        divs = response.xpath('//div[@id="mulu"]/div[3]/div[@class="DivTr"]/div[@class="DivTd"]')
        for j in divs:
            hrefs = j.xpath('./a/@href').get()
            if hrefs:
                url = "https:" + hrefs
                item['titles'] = j.xpath('./a/text()').get()
                yield scrapy.Request(
                    url=url,
                    callback=self.infoo,
                    meta={"item": deepcopy(item)}
                )

    def infoo(self,response,**kwargs):
        item = response.meta['item']
        divv = response.xpath('//div[@class="noveContent"]')
        for x in divv:
            text = x.xpath('./p//text()').getall()
            item['texts'] = "\n".join(text)
            print(item)
            yield item
