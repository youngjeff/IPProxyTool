#-*- coding: utf-8 -*-

from validator import Validator


class MSpider(Validator):
    name = 'm1905'

    def __init__(self, name = None, **kwargs):
        super(ITSpider, self).__init__(name, **kwargs)

        self.timeout = 10
        self.urls = [
            'http://www.1905.com/mdb/film/list/',
            
        ]

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            'Host': 'css.static.m1905.cn',
            # 'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        }

        self.init()
