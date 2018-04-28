#!./venv/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
import requests, json
from config import config, response, token

card = Blueprint('card', __name__)

@card.route('/', methods = ['POST'])
def main():
    content = request.form['text']
    args = content.split(' ')
    if (args[0] == ''):
        return cash()
    return record()

def record():
    id = request.form['user_id']
    if id not in token:
        response['text'] = '请先绑定账号'
        return jsonify(response)
    data = {
        'sno': token[id]['sno'],
        'pwd': token[id]['pwd'],
    }
    url = 'http://api.wegdufe.com:82/index.php?r=card/current-cash'
    r = requests.post(url, data = data)
    message = json.loads(r.text)
    data['cardNum'] = message['data']['cardNum']
    url = 'http://api.wegdufe.com:82/index.php?r=card/consume-today'
    r = requests.post(url, data = data)
    message = json.loads(r.text)
    content = u"""| 交易时间 | 交易商户 | 交易额 | 余额 |
    |:-:|:-:|:-:|:-:|
    """
    for value in message['data']:
        content += '|' + value['time'] + '|' + value['shop'] + '|' + value['change'] + '|' + value['cash'] + '|' + '\n'
    response['text'] = content
    return jsonify(response)

def cash():
    id = request.form['user_id']
    if id not in token:
        response['text'] = '请先绑定账号'
        return jsonify(response)
    data = {
        'sno': token[id]['sno'],
        'pwd': token[id]['pwd'],
    }
    url = 'http://api.wegdufe.com:82/index.php?r=card/current-cash'
    r = requests.post(url, data = data)
    message = json.loads(r.text)
    content = u"""| 卡号 | 余额 | 卡状态 | 检查状态 | 挂失状态 | 冻结状态 |
    |:-:|:-:|:-:|:-:|:-:|:-:|
    """
    value = message['data']
    content += '|' + value['cardNum'] + '|' + value['cash'] + '|' + value['cardState'] + '|' + value['checkState'] + '|' + value['lossState'] + '|' + value['freezeState'] + '|'
    response['text'] = content
    return jsonify(response)

if __name__ == '__main__':
    data = {
        'sno': config['sno'],
        'pwd': config['pwd'],
    }
    url = 'http://api.wegdufe.com:82/index.php?r=card/current-cash'

    r = requests.post(url, data = data)
    print r.text
    message = json.loads(r.text)
    print message['data']['cardNum']