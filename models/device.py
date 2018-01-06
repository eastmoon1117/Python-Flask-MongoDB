#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db

# 类名定义 collection
class Device1(db.Document):
    # 字段
    devicename = db.StringField()
    macaddr = db.StringField()
    
    def __str__(self):
        return "devicename:{} - macaddr:{}".format(self.devicename, self.macaddr)

