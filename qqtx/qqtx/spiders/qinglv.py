import scrapy
from qqtn.items import QqtnItem


class QinglvSpider(scrapy.Spider):
    name = 'qinglv'
    allowed_domains = ['www.qqtn.com']
    start_urls = ['https://www.qqtn.com/tx/qinglvtx_1.html']

    def parse(self, response, **kwargs):
        response = response.xpath('//ul[@class="g-gxlist-imgbox"]/li')
        next_page = response.xpath('//div[@class="tsp_nav"]/a[@class="tsp_next"]/@href').get()
        if next_page:
            next_page = "https://www.qqtn.com/" + next_page
            print(next_page)
            yield scrapy.Request(
                url=next_page,
                callback=self.parse
            )

        for i in response:
            item = QqtnItem()
            src = "https://www.qqtn.com" + i.xpath('./a/@href').get()
            item['title'] = i.xpath('./a/strong/text()').get()

            yield scrapy.Request(
                url=src,
                callback=self.jiexi,
                meta={'item': item}
            )

    def jiexi(self, response, **kwargs):
        item = response.meta['item']
        div = response.xpath('//div[@id="content"]/p')
        for j in div:
            url_src = j.xpath('./img/@src').get()
            if url_src:
                item['src'] = url_src
                yield item
