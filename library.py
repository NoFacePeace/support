#!./venv/bin/python
# -*- coding: UTF-8 -*-

import requests, json
from flask import Blueprint, request, jsonify
from config import config, response, token
from bs4 import BeautifulSoup

library = Blueprint('library', __name__)

@library.route('/', methods = ['POST'])
def main():
    content = request.form['text']
    args = content.split(' ')
    if (args[0] == 'history'):
        return history()
    if (args[0] == 'search'):
        return search_book(args)
    return borrow_book()

def history():
    id = request.form['user_id']
    if id not in token:
        response['text'] = '请先绑定账号'
        return jsonify(response)
    data = {
        'sno': token[id]['sno'],
        'pwd': token[id]['pwd'],
    }
    url = 'http://api.wegdufe.com:82/index.php?r=opac/borrowed-book'
    r = requests.post(url, data = data)
    print r.text
    message = json.loads(r.text)
    content = u"""| 条码号 | 书名 | 作者 | 借阅时间 | 已归还时间 | 已续借次数 | 馆藏地 |
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    """
    for value in message['data']:
        content += '|' + value['barId'] + '|' + value['name'] + '|' + value['author'] + '|' + value['borrowedTime'] + '|' + value['returnTime'] + '|' + str(value['renewTimes']) + '|' + value['location'] + '|' + '\n'
    response['text'] = content
    return jsonify(response)

def borrow_book():
    id = request.form['user_id']
    if id not in token:
        response['text'] = '请先绑定账号'
        return jsonify(response)
    data = {
        'sno': token[id]['sno'],
        'pwd': token[id]['pwd'],
    }
    url = 'http://api.wegdufe.com:82/index.php?r=opac/current-book'
    r = requests.post(url, data = data)
    message = json.loads(r.text)
    content = u"""| 条码号 | 书名 | 作者 | 借阅时间 | 应归还时间 | 已续借次数 | 馆藏地 |
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    """
    for value in message['data']:
        content += '|' + value['barId'] + '|' + value['name'] + '|' + value['author'] + '|' + value['borrowedTime'] + '|' + value['returnTime'] + '|' + value['renewTimes'] + '|' + value['location'] + '|' + '\n'
    response['text'] = content
    return jsonify(response)

def search_book(args):
    params = {
        'q': args[1],
        't': 'any',
        'page': 1,
    }
    if (len(args) == 3):
        params['page'] = args[2]
    url = 'http://weixin.library.gdufe.edu.cn/m/weixin/wsearch.action'
    res = requests.get(url = url, params = params)
    book = []
    soup = BeautifulSoup(res.text, "html.parser")
    arr = soup.find_all(attrs = {'class': 'weui_media_title'})
    for title in arr:
        tmp = {}
        tmp['title'] = title.string
        book.append(tmp)
    arr = soup.find_all(attrs= {'class': 'weui_media_desc'})
    i = 0
    for desc in arr:
        book[i]['desc'] = desc.string
        i += 1
    i = 0
    arr = soup.find_all(attrs= 'weui_media_info_meta')
    for info in arr:
        book[i]['info'] = info.string
        i += 1
    content = u"""| 书名 | 出版信息 | 详情 |
    |:-:|:-:|:-:|
    """
    for value in book:
        content += '|' + value['title'] + '|' + value['desc'] + '|' + value['info'] + '|' + '\n'
    response['text'] = content
    return jsonify(response)

if __name__ == '__main__':
    pass