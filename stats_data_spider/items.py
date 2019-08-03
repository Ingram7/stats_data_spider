# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class Class1_Item(scrapy.Item):
    # 省级
    name = Field()
    # code = Field()

class Class2_Item(scrapy.Item):
    # 市级
    name = Field()
    code = Field()

class Class3_Item(scrapy.Item):
    # 区级
    name = Field()
    code = Field()

class Class4_Item(scrapy.Item):
    # 街道
    name = scrapy.Field()
    code = scrapy.Field()

class Class5_Item(scrapy.Item):
    # 居委会
    name = scrapy.Field()
    code = scrapy.Field()
    code2 = scrapy.Field()
