# -*- coding: utf-8 -*-
# @Time    : 2019-12-19 11:16
# @Author  : peiyu
# @Email   : lvegod@163.com
# @File    : dmoz_spider.py
# @Software: PyCharm

import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)