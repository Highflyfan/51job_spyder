# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class JobSpiderPipeline(object):
    def process_item(self, item, spider):
        with open('data.csv', 'a+', newline='') as file:
            fname = [i for i in item]
            writer = csv.DictWriter(file, fname)
            writer.writerow(item)
