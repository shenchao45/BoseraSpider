#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :02/01/2018 3:39 PM
# @Author   :shenchao
# @File     :main.py
from scrapy import cmdline
# 0 0 * * * *
cmdline.execute('scrapy crawl bosera'.split())