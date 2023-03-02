import re
import time
import traceback
from shjd.items import ShjdItem
import scrapy


class ShSpider(scrapy.Spider):
    name = 'sh'
    allowed_domains = ['cc.focus.cn']
    start_urls = ['https://wh.focus.cn/loupan/p1/']
    """意思是每次循环都将f_url清空为0"""
    page = 1
    f_url = ''

    def parse(self, response, **kwargs):
        div_text = response.xpath('//div[@class="s-lp-all "]')
        for div in div_text:
            item = ShjdItem()
            item['title'] = div.xpath('./div[@class="list"]/div[@class="txt-center"]/div/a/text()').get()
            zhuang = div.xpath('./div[@class="list"]/div[@class="txt-center"]/div/span/text()').get()
            item["zhuantai"] = zhuang.strip()
            dizhi = div.xpath('./div[@class="list"]/div[@class="txt-center"]/p[@class="location"]/span/text()').get()
            weizhi = dizhi.strip()
            item["weizhi"] = weizhi
            mianji = div.xpath('./div[@class="list"]/div[@class="txt-center"]/div[@class="huxing"]/span/text()').get()
            if mianji:
                item["mianji"] = mianji.strip()
            geshi = div.xpath(
                './div[@class="list"]/div[@class="txt-center"]/div[@class="huxing"]/span[@class="huxing-info"]//text()').getall()
            """根据长度来处理广告"""
            if geshi:
                if len(geshi) > 9:
                    item["huxing"] = geshi[2] + geshi[5] + geshi[8]
                elif len(geshi) > 5:
                    item['huxing'] = geshi[2] + geshi[5]
                else:
                    pass
            item['dianhua'] = div.xpath(
                './div[@class="list"]/div[@class="txt-center"]/div[@class="tel"]/span[@class="txt"]/text()').get()
            item['jiage'] = div.xpath('./div[@class="list"]/div[@class="txt-right"]/span/text()').get() + "元/平米"
            yield item

        """
        self.page的初始值为1,
        只要条件成立就执行里面的代码,发送请求
        """
        if self.page == 1:
            self.f_url = response.xpath('//a[@class="   hide"]/@href').get()
            self.page += 1

            try:
                couunt = self.f_url.split("/")[-2].strip("p")
                print(couunt)
                for i in range(2, int(couunt) + 2):
                    ur = "https://wh.focus.cn/loupan/p{}/".format(i)
                    print(ur)
                    yield scrapy.Request(url=ur, callback=self.parse, dont_filter=True)


            except Exception as f:
                print("结束")
                print(f)
        """这里是条件不满足的时候发送的代码"""
