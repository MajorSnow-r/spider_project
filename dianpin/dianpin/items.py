# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DianpinItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    pingjia = scrapy.Field()
    pingfen = scrapy.Field()
    dianpin = scrapy.Field()
    baoguang = scrapy.Field()
    name = scrapy.Field()
    colour = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
    pass
