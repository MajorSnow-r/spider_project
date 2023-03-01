import scrapy
from anjke.items import AnjkeItem


class AjkSpider(scrapy.Spider):
    name = 'ajk'
    allowed_domains = ['sip.fang.anjuke.com']
    yh = input("输入要获取城市的拼音:")
    if yh.encode('utf-8').isalpha():
        start_urls = ['https://{}.fang.anjuke.com/loupan/all/'.format(yh)]
    else:
        print("输入错误")
        yh = input("请重新输入拼音:")

    def parse(self, response, **kwargs):
        div_mod = response.css('div.item-mod')
        for css_a in div_mod:
            item = AnjkeItem()
            """名称"""
            title = css_a.css('a > span.items-name::text').get()
            if title:
                item["title"] = title
                print(title+"爬取成功")
                """地址"""
                wzhi = css_a.css('a > span.list-map::text').get()
                wzhi_split = wzhi.split("]")
                item["diqu"] = wzhi_split[0].strip("[")
                item["dizhi"] = wzhi_split[1]
                """户型"""
                huxings = css_a.css('a.huxing > span::text').getall()
                if huxings:
                    item["huxing"] = "/".join(huxings[0:-1])
                    item["mianji"] = huxings[-1]
                """状态"""
                zhuangtais = css_a.css('i.status-icon::text').getall()
                zhuangtaiss = css_a.css('span.tag::text').getall()
                zhuang = zhuangtais + zhuangtaiss
                zhuangtai = "/".join(zhuang)
                item["zhuangtai"] = zhuangtai
                """价格"""
                jiage = css_a.css('p > span::text').getall()
                if jiage:
                    item['junjia'] = jiage[0] + "元/平"
                yield item

        """翻页处理"""
        try:
            fy_url = response.css('a.next-page::attr(href)').get()

            yield scrapy.Request(url=fy_url, callback=self.parse, dont_filter=True, meta={'dont_redirect': True})
        except Exception as f:
            print("爬取结束")
