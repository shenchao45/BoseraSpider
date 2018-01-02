# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from boseraSpider.util.excel import _Excel
from xlwt import *
import datetime


class BoseraspiderPipeline(object):
    row_index = 0

    def __init__(self):
        self.workBook = Workbook(encoding='utf-8')
        header_2_style = _Excel.get_header_2_style()
        self.sheet = self.workBook.add_sheet('统计')
        _Excel.append_row(self.sheet, 0, header_2_style, 3000, u'日期', u'万份收益', u'最近7日的年化收益率', u'最近30日的年化收益率',
                          u'今年以来的年化收益率', u'成立以来的收益率')
        self.row_index += 1

    def process_item(self, item, spider):
        _Excel.append_row(self.sheet, self.row_index, None, None, item['date'], item['fundIncome'], item['yield_'],
                          item['yield30Days'], item['yieldThisYear'], item['totalYield'])
        self.row_index += 1
        return item

    def close_spider(self, spider):
        self.workBook.save((datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d') + '产品收益率.xls')
