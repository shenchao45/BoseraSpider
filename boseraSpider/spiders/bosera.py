# -*- coding: utf-8 -*-
import scrapy
from boseraSpider.items import BoseraspiderItem
import json
import datetime
import pandas as pd


class BoseraSpider(scrapy.Spider):
    name = 'bosera'
    allowed_domains = ['bosera.com']
    pageNo = 1
    pageSize = 10
    startDate = (
            datetime.datetime.now() - datetime.timedelta(days=1) - pd.tseries.offsets.DateOffset(months=3)).strftime(
        '%Y-%m-%d')
   a endDate = datetime.datetime.now().strftime('%Y-%m-%d')
    url = 'http://www.bosera.com/fund/fundHisDetail.json?pageNo=%s&pageSize=%s&fundCode=000730&startDate=%s&endDate=%s'
    start_urls = [url % (pageNo, pageSize, startDate, endDate)]

    def parse(self, response):
        data = json.loads(response.text, encoding='utf-8')['data']['resultList']
        if len(data) <= 0:
            return
        for each in data:
            item = BoseraspiderItem()
            item["date"] = each["date"]
            item["fundIncome"] = each["fundIncome"]
            item["yield_"] = each["yield"]
            item["yield30Days"] = each["yield30Days"]
            item["yieldThisYear"] = each["yieldThisYear"]
            item["totalYield"] = each["totalYield"]
            yield item
        self.pageNo += 1
        yield scrapy.Request(self.url % (self.pageNo, self.pageSize, self.startDate, self.endDate), callback=self.parse)
