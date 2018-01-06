#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from flask import Flask, jsonify, request, abort
from datetime import datetime
from models.device import Device1

tasks = [
    {
        'id': 1,
        'price': 10.8,
        'title': 'test1',
        'done': False,
    },
    {
        'id': 2,
        'price': 10.9,
        'title': 'test2',
        'done': True,
    }

]

@app.route('/todo/api/v1/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'devicename' in request.json:
        print(request)
        abort(400)
    
    #task = {
    #    'id': tasks[-1]['id'] + 1,
    #    'title': request.json['title'],
    #    'price': request.json['price'],
    #    'done': False
    #}
    #tasks.append(task)
    device = Device1(devicename=request.json['devicename'], macaddr=request.json['macaddr']).save();
    return jsonify({'device': Device1.objects.all()}), 201
    #return jsonify({'task': tasks}), 201

@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    device = Device1.objects(devicename='device1').first()
    device.update(devicename="device9")
    print device['devicename'] + ":" + device['macaddr']
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1')
def index():
    return "Hello, World!"

