# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WyzpItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    bumen = scrapy.Field()
    zhice  = scrapy.Field()
    xli  = scrapy.Field()
    rshu  = scrapy.Field()
    dizhi  = scrapy.Field()
    jingyan = scrapy.Field()
    ganw_miaoshu = scrapy.Field()
    gangw_zhize= scrapy.Field()
    pass
