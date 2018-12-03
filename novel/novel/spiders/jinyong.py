# -*- coding: utf-8 -*-
import scrapy
from novel.items import NovelItem

class JinyongSpider(scrapy.Spider):
    name = 'jinyong'
    allowed_domains = ['www.jinyongwang.com']
    start_urls = ['http://www.jinyongwang.com/book/']
    base_url = 'http://www.jinyongwang.com'

    def parse(self, response):
        item = NovelItem()
        title_list = response.xpath('//p[@class="title"]/a')
        # print(title_list)
        for title in title_list:

            item['novel_title'] = title.xpath('.//text()').get()
            href = title.xpath('.//@href').get()
            novel_url = self.base_url + href
            print(item['novel_title'])
            yield scrapy.Request(url=novel_url,callback=self.parse_content,meta={"item":item})


    def parse_content(self,response):
        item = response.meta['item']
        # print(item)
        part_list = response.xpath('//ul[@class="mlist"]/li/a')
        for parts in part_list:
            item['part'] = parts.xpath('.//text()').get()
            href = parts.xpath('.//@href').get()
            url = self.base_url+href
            # print(item)
            yield scrapy.Request(url=url,callback=self.parse_detail,meta={"item":item})

    def parse_detail(self,response):
        item = response.meta["item"]
        item['content']= response.xpath('string(//*[@id="vcon"]/p)').get()
        print(item)
        yield item








