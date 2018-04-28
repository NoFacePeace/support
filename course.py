#!./venv/bin/python
# -*- coding: UTF-8 -*-

from flask import Blueprint, request, jsonify
from config import config, response, token

import requests, json

course = Blueprint('course', __name__)

@course.route('/', methods = ['POST'])
def main():
    id = request.form['user_id']
    if id not in token:
        response['text'] = '请先绑定账号'
        return jsonify(response)
    url = 'http://api.wegdufe.com:82/index.php?r=jw/get-schedule'
    content = request.form['text']
    args = content.split(' ')
    data = {
        'sno': token[id]['sno'],
        'pwd': token[id]['pwd'],
    }
    if (len(args) == 1):
        data['stu_time'] = args[0]
    if (len(args) >= 2):
        data['stu_time'] = args[0]
        data['week'] = args[1]
    r = requests.post(url, data = data)
    content = """| 课程名 | 老师 | 周数 | 教室 | 星期 | 开始节 | 结束节 |
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    """
    message = json.loads(r.text)
    for value in message['data']:
        content += '|' + value['name'].encode('utf-8') + '|' + value['teacher'].encode('utf-8') + '|' + value['period'].encode('utf-8') + '|' + value['location'].encode('utf-8') + '|' + str(value['dayInWeek']) + '|' + str(value['startSec']) + '|' + str(value['endSec']) + '|' + '\n'
    response['text'] = content
    return jsonify(response)

if __name__ == '__main__':
    data = {
        'sno': config['sno'],
        'pwd': config['pwd'],
        'stu_time': '2014-2015-2'
    }
    url = 'http://api.wegdufe.com:82/index.php?r=jw/get-schedule'
    r = requests.post(url, data = data)
    content = json.loads(r.text)
    print content['data']