# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode
from images360.items import ImageItem

import scrapy


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def start_requests(self):
        data = {'ch': 'photography', 'listtype': 'new', 'temp': '1'}
        base_url = 'https://image.so.com/zj?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        if 'list' in result.keys():
            for image in result['list']:
                item = ImageItem()
                item['url'] = image.get('qhimg_url')
                item['title'] = image.get('group_title')
                yield item





