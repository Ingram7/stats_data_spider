# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from stats_data_spider.settings import LOCAL_MONGO_HOST,LOCAL_MONGO_PORT,DB_NAME
import pymongo
from pymongo.errors import DuplicateKeyError
from stats_data_spider.items import *

class MongoPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)
        # 数据库名
        db = client[DB_NAME]
        # 数据库的 集合 名
        self.provincetr = db["provincetr"]
        self.citytr = db["citytr"]
        self.countytr = db["countytr"]
        self.towntr = db["towntr"]
        self.villagetr = db["villagetr"]


    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, Class1_Item):
            self.insert_item(self.provincetr, item)
        elif isinstance(item, Class2_Item):
            self.insert_item(self.citytr, item)
        elif isinstance(item, Class3_Item):
            self.insert_item(self.countytr, item)
        elif isinstance(item, Class4_Item):
            self.insert_item(self.towntr, item)
        elif isinstance(item, Class5_Item):
            self.insert_item(self.villagetr, item)

        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            """
            说明有重复数据
            """
            pass