#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db':   'todoApp',
    'host': '127.0.0.1',
    'port': 27017
}

#app.config.from_pyfile('config.json')
db = MongoEngine(app)

#数据库对应的模型
#import models

#api的业务逻辑
import controllers

