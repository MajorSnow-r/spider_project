# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShjdItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    zhuantai = scrapy.Field()
    weizhi = scrapy.Field()
    mianji = scrapy.Field()
    huxing = scrapy.Field()
    dianhua = scrapy.Field()
    jiage= scrapy.Field()
    pass
