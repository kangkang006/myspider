# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['biz.touchev.com/']
    start_urls = ['http://biz.touchev.com/industry_notice?cat=taxfree_bev&group=all&keyword=&page=all']
    # url = "http://biz.touchev.com/industry_notice?cat=taxfree_bev&group=all&keyword=&page="
    # offset = 1
    # start_urls = [url + str(offset)]

    def parse(self, response):
        car_list = response.xpath('//*[@id="tab5"]/table/tbody/tr')
        for each in car_list:
            item = MyspiderItem()
            data = each.xpath('./td').extract()
            # print(data)
            for i in range(11):
                if i == 0:
                    item['batch'] = data[i][4:-5].replace(u'\xa0', u'')
                elif i == 1:
                    item['sn'] = data[i][4:-5].replace(u'\xa0', u'')
                elif i == 2:
                    item['company_name'] = data[i][4:-5].replace(u'\xa0', u'')
                elif i == 3:
                    item['kind'] = data[i][4:-5].replace(u'\xa0', u'')
                elif i == 4:
                    item['vehicle_model'] = data[i][4:-5].replace(u'\xa0', u'')
                elif i == 5:
                    item['common_name'] = data[i][4:-5].replace(u'\xa0', u'')
                elif i == 6:
                    item['nedc'] = data[i][4:-5].replace(u'\xa0', u'')
                elif i == 7:
                    item['mass'] = data[i][4:-5].replace(u'\xa0', u'')
                elif i == 8:
                    item['battery_mass'] = data[i][4:-5].replace(u'\xa0', u'')
                elif i == 9:
                    item['battery_energy'] = data[i][4:-5].replace(u'\xa0', u'')
                elif i == 10:
                    item['comment'] = data[i][4:-5].replace(u'\xa0', u'')
            yield item

        # if self.offset < 235:
        #     self.offset += 1
        # yield scrapy.Request(self.url + str(self.offset), callback=self.parse, dont_filter=True)

