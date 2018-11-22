# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from douban_actors.data_clean import get_clean
#from fake_useragent import UserAgent
import pandas as pd
import numpy as np
import re

g = get_clean()
result = g.mapping()

### 时间分布
### 模仿那个项目写一个完整的豆瓣scrapy爬取系统
### ---半小时复习middleware，半小时把完整url导出来，RandomUserAgentMiddleware
### ---写出分布式的scrapy，加快爬取速度


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']
    result = result

    def start_requests(self):
        for url in self.result[0:1]:
            if url != "None":
                yield Request("https://movie.douban.com/celebrity/1053581/movies?sortby=time&format=text",self.parse)

    def parse(self, response):
        max_page_str = response.xpath('//*[@id="content"]/h1/text()').re("\d+")[0]
        max_page = int(max_page_str)
        page = int(max_page/25) + 1
        print(page)

    def parse_second_layer(self,response):
        pass

