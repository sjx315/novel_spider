# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class NovelPipeline(object):
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='novel',
                                    charset='utf8')

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into novel(novel_title,part,content) VALUES(%s,%s,%s)'
        self.cursor.execute(sql,(item["novel_title"],item['part'],item['content']))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
