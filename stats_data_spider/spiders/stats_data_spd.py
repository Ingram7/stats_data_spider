# -*- coding: utf-8 -*-

from scrapy import Request
from ..items import *
import re

class StatsDataSpdSpider(scrapy.Spider):
    name = 'stats_data_spd'
    allowed_domains = ['stats.gov.cn']
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html']


    def parse(self, response):
        # 省级
        for node in response.xpath('//tr[@class="provincetr"]/td'):
            item = Class1_Item()
            item['name'] = node.xpath('./a/text()').extract()[0]
            url1 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/'
            url = url1 + node.xpath('./a/@href').extract()[0]
            yield item
            yield Request(url, callback=self.parse2, )

    def parse2(self, response):
        # 市级
        for node in response.xpath('//tr[@class="citytr"]'):
            item = Class2_Item()
            item['name'] = node.xpath('./td[2]/a/text()').extract()[0]
            item['code'] = node.xpath('./td[1]/a/text()').extract()[0]
            url1 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/'
            url = url1 + node.xpath('./td[2]/a/@href').extract()[0]
            yield item
            yield Request(url, callback=self.parse3)

    def parse3(self, response):
        # 区级
        for node in response.xpath('//tr[@class="countytr"]'):
            item = Class3_Item()
            name = node.xpath('./td[2]/a/text()').extract()
            if name :
                item['name'] = node.xpath('./td[2]/a/text()').extract()[0]
                item['code'] = node.xpath('./td[1]/a/text()').extract()[0]

                url1 = response.request.url
                url1 = re.split('/\d+.html', url1)[0]

                url = url1 + '/' + node.xpath('./td[2]/a/@href').extract()[0]
                yield item
                yield Request(url, callback=self.parse4)

    def parse4(self, response):
        # 街道
        for node in response.xpath('//tr[@class="towntr"]'):
            item = Class4_Item()
            item['name'] = node.xpath('./td[2]/a/text()').extract()[0]
            item['code'] = node.xpath('./td[1]/a/text()').extract()[0]

            url1 = response.request.url
            url1 = re.split('/\d+.html', url1)[0]

            url = url1 + '/' + node.xpath('./td[2]/a/@href').extract()[0]
            yield item
            yield Request(url, callback=self.parse5)

    def parse5(self, response):
        # 居委会
        for node in response.xpath('//tr[@class="villagetr"]'):
            item = Class5_Item()
            item['name'] = node.xpath('./td[3]/text()').extract()[0]
            item['code'] = node.xpath('./td[1]/text()').extract()[0]
            item['code2'] = node.xpath('./td[2]/text()').extract()[0]
            yield item
