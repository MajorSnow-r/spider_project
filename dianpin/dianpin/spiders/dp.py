import scrapy
from dianpin.items import DianpinItem
from copy import deepcopy

# from scrapy_redis.spiders import RedisSpider
from scrapy_redis.spiders import RedisSpider


class DpSpider(RedisSpider):
    name = 'dp'
    allowed_domains = ['dianping.360.cn']
    # start_urls = ['https://dianping.360.cn//category/5?page=1']

    redis_key = "key"

    """解析首页的方法"""
    def parse(self, response, **kwargs):
        divs = response.xpath('//div[@id="cg-right"]/div[@class="sites"]')
        for div in divs:
            item = DianpinItem()
            item['title'] = div.xpath('./div[@class="sites-tit"]/a/text()').get()
            item['pingjia'] = div.xpath('./div[@class="sites-inner"]/span[@class="percent"]/em/text()').get()
            item['pingfen'] = div.xpath('./div[@class="sites-inner"]/span[@class="num"]//text()').get()
            item['dianpin'] = div.xpath('./div[@class="sites-ft"]/a/em/text()').get()
            item['baoguang'] = div.xpath('./div[@class="sites-ft"]/a[2]/text()').get()

            """解析出来的详情页url发送请求"""
            href = div.xpath('./div[@class="sites-tit"]/a/@href').get()
            xiang_url = 'https://dianping.360.cn' + href
            yield scrapy.Request(url=xiang_url, callback=self.xiang_parse, meta={'item': deepcopy(item)})

        """首页翻页"""
        if response.xpath('//div[@class="page"]/fieldset/a[@class="next"]'):
            fieldset = response.xpath('//div[@class="page"]/fieldset/a[@class="next"]/@href').get()
            urls = 'https://dianping.360.cn/' + fieldset
            print("翻页url=", urls)
            yield scrapy.Request(url=urls, callback=self.parse)
        else:
            print("翻页到头了")

    """解析详情页的方法"""

    def xiang_parse(self, response, **kwargs):
        item = response.meta['item']
        div = response.xpath('//div[@class="ce-list"]/div[@class="ce-item"]')
        """
        判断详情页是否有数据
        如果详情页没有数据就写入空
        """
        if div:
            for i in div:
                item['name'] = i.xpath('./div[@class="cont"]/div[@class="cont-hd"]/a/text()').get()
                yanse = i.xpath('./div[@class="cont"]/div[@class="cont-hd"]/span//text()').getall()
                item['colour'] = "".join(yanse)
                item['text'] = i.xpath('./div[@class="cont"]/div[@class="cont-bd"]/text()').get()
                item['date'] = i.xpath('./div[@class="cont"]/div[@class="cont-ft"]/div[2]/text()').get()
                yield item
        else:
            item['name'] = "空"
            item['colour'] = "空"
            item['text'] = "空"
            item['date'] = "空"
            yield item

        """详情页翻页"""
        xiang_fieldset = response.xpath('//div[@class="page"]/fieldset/a[@class="next"]/@href').get()
        try:
            xiang_url = 'https://dianping.360.cn' + xiang_fieldset
            print("详情页翻页", xiang_url)
            yield scrapy.Request(url=xiang_url, callback=self.xiang_parse, meta={'item': deepcopy(item)})
            """因为每一页的详情页都不统一,所以这里用异常捕获来处理"""
        except Exception as f:
            pass
