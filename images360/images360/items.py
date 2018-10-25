# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Images360Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ImageItem(scrapy.Item):
    # define the fields for your item here like:

    # 每个item存储到数据库中的表格中，定义表格的名称
    collection = table = 'images'
    url = scrapy.Field()
    title = scrapy.Field()

