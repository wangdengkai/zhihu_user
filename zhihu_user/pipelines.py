# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class ZhihuUserPipeline(object):
    def process_item(self, item, spider):
        return item


class MogoPipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db


    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri =crawler.settings.get("MONGO_URI"),
            mongo_db = crawler.settings.get("MONGO_DATABASE","items")
        )mtelf.client.close()


    def process_item(self,item,spider):
        self.db['user'].update(
            {'url_token':item['url_token']}

        ,{'$set':item},
            True
        )

        return item