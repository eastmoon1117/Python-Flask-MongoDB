#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db
from models.device import Device1

# 类名定义 collection
class User(db.Document):
    # 字段
    name = db.StringField(max_length=30, required=True)
    password = db.StringField(max_length=30, min_length=6, required=True)
    phone = db.StringField()
    device = db.ReferenceField(Device1)
    devices = db.ListField(db.ReferenceField(Device1))
    emdevices = db.ListField(db.EmbeddedDocumentField('Device1'))

    def __str__(self):
        return "name:{} - phone:{}".format(self.name, self.phone)
    
