#!./venv/bin/python
# -*- coding: UTF-8 -*-

from flask import Blueprint, jsonify, request
from config import response, config, token
import requests
import json

grade = Blueprint('grade', __name__)

@grade.route('/', methods = ['POST'])
def main():
    id = request.form['user_id']
    if id not in token:
        response['text'] = '请先绑定账号'
        return jsonify(response)
    url = 'http://api.wegdufe.com:82/index.php?r=jw/get-grade'
    content = request.form['text']
    args = content.split(' ')
    data = {
        'sno': token[id]['sno'],
        'pwd': token[id]['pwd'],
    }
    if (len(args) > 0):
        data['stu_time'] = args[0]
    r = requests.post(url, data = data)
    content = """| 课程名 | 总分 | 学分 | 平时成绩 | 期末成绩 |
    |:-:|:-:|:-:|:-:|:-:|
    """
    message = json.loads(r.text)
    for value in message['data']:
        content += '|' + value['name'].encode('utf-8') + '|' + str(value['score']) + '|' + str(value['credit']) + '|' + str(value['dailyScore']) + '|' + str(value['paperScore']) + '|' + '\n'
    response['text'] = content
    return jsonify(response)

if __name__ == '__main__':
    data = {
        'sno': config['sno'],
        'pwd': config['pwd'],
    }
    url = 'http://api.wegdufe.com:82/index.php?r=jw/get-grade'
    r = requests.post(url, data = data)
    print r.text
    