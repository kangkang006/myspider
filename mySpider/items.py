# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    batch = scrapy.Field()
    sn = scrapy.Field()
    company_name = scrapy.Field()
    kind = scrapy.Field()
    vehicle_model = scrapy.Field()
    common_name = scrapy.Field()
    nedc = scrapy.Field()
    mass = scrapy.Field()
    battery_mass = scrapy.Field()
    battery_energy = scrapy.Field()
    comment = scrapy.Field()

