#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构
import re

pattern = re.compile(r'\| *(?P<year>\d+)年.*\| *(?P<size>\d+\.?\d*)平米')
id_pattern = re.compile(r'/(?P<id>\d+)\.html')


class ErShou(object):
    def __init__(self, district, area, name, price, desc, pic, href):
        self.district = district
        self.area = area
        self.price = price
        self.name = name
        self.desc = desc
        self.pic = pic
        self.href = href

    def text(self):
        self.price = self.price[:-1]
        matchRes = re.search(pattern, str(self.desc))
        if matchRes is None:
            self.year, self.size, self.avg_price = -1, -1, -1
        else:
            groups = matchRes.groups()
            self.year, self.size = groups[0], groups[1]
            try:
                self.avg_price = round(float(self.price) / float(self.size), 1)
            except ValueError:
                self.avg_price = -1;
                pass
        self.id = re.search(id_pattern, str(self.href)).groups()[0] # houseId
        return '"' + str(self.id) + '"' + "," + \
               '"' + self.district + '"' + "," + \
               '"' + self.area + '"' + "," + \
               '"' + self.name + '"' + "," + \
               '"' + str(self.size) + '"' + "," + \
               '"' + str(self.price) + '"' + "," + \
               '"' + str(self.avg_price) + '"' + "," + \
               '"' + str(self.year) + '"' + "," + \
               '"' + self.desc + '"' + "," + \
               '"' + self.pic + '"'
