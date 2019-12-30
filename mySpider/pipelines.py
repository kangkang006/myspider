# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb

class MyspiderPipeline(object):
    def __init__(self):
        # self.filename = open("car.json", "w")
        self.connect = MySQLdb.connect(host='127.0.0.1', user='root', passwd='N7102io', db='scrapy_db', charset='utf8')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.filename.write(jsontext)
        # return item
        sql = """insert into freetax(batch, sn, company_name, kind, vehicle_model, common_name, nedc, mass, battery_mass, 
        battery_energy, note) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        self.cursor.execute(sql, (item['batch'], item['sn'], item['company_name'], item['kind'], item['vehicle_model'],
                                  item['common_name'], item['nedc'], item['mass'], item['battery_mass'], item['battery_energy'],
                                  item['comment']))
        self.connect.commit()

    def close_spider(self, spider):
        # self.filename.close()
        self.cursor.close()
        self.connect.close()
