# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjkeItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    diqu = scrapy.Field()
    dizhi = scrapy.Field()
    huxing = scrapy.Field()
    mianji = scrapy.Field()
    zhuangtai = scrapy.Field()
    junjia = scrapy.Field()
    pass
