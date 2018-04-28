#!./venv/bin/python
# -*- coding: UTF-8 -*-

from flask import Blueprint, jsonify, request
import requests, json
from config import config, response, token

info = Blueprint('info', __name__)

@info.route('/', methods = ['POST'])
def main():
    id = request.form['user_id']
    if id not in token:
        response['text'] = '请先绑定账号'
        return jsonify(response)
    data = {
        'sno': token[id]['sno'],
        'pwd': token[id]['pwd'],
    }
    res = requests.post('http://api.wegdufe.com:82/index.php?r=jw/get-basic', data = data)
    arr = json.loads(res.text)
    content = ''
    for key, value in arr['data'].iteritems():
        content += key + ' : ' + value + '\n'
    response['text'] = content
    return jsonify(response)


if __name__ == '__main__':
    pass