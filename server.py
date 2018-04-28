#!./venv/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, jsonify, request
from todo import todo
from mail import mail
from info import info
from grade import grade
from course import course
from card import card
from library import library
from bind import bind
import json, requests

app = Flask(__name__)

app.register_blueprint(todo, url_prefix = '/todo')
app.register_blueprint(mail, url_prefix = '/mail')
app.register_blueprint(info, url_prefix = '/info')
app.register_blueprint(grade, url_prefix = '/grade')
app.register_blueprint(course, url_prefix = '/course')
app.register_blueprint(card, url_prefix = '/card')
app.register_blueprint(library, url_prefix = '/library')
app.register_blueprint(bind, url_prefix = '/bind')

url = 'http://127.0.0.1:8065/hooks/6wyh1cu79bn8jd3c7e7pw47yoy'
data = ''

@app.route('/', methods = ['GET', 'POST'])
def main():
    res = request.data
    args = json.loads(res)
    if args['object_kind'] == 'push':
        push(args)
    if args['object_kind'] == 'issue':
        issue(args)
    if args['object_kind'] == 'note':
        note(args)
    return 'error'

def push(args):
    data = '{"text": "代码库更新了"}'
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, data= data, headers = headers)
    print 'ssh <域名>'
    print 'cd <folder>'
    print 'git pull <域名>'
    print 'systemctl stop nginx'
    print 'systemctl start nginx'
    return 'error'

def issue(args):
    data = '{"text": "有问题提交"}'
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, data= data, headers = headers)
    print res
    return 'error'

def note(args):
    data = '{"text": "有新的评论"}'
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, data= data, headers = headers)
    print res
    return 'error'

if __name__ == '__main__':
    app.debug = True
    app.run(port= 8088)