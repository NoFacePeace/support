#!./venv/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, Blueprint
from config import config, response, token

bind = Blueprint('bind', __name__)

@bind.route('/', methods = ['POST'])
def main():
    text = request.form['text']
    args = text.split(' ')
    if args[0] == 'logout':
        return logout()
    if args[0] == 'online':
        return online()
    return login(args)

def login(args):
    key = request.form['user_id']
    token[key] = {}
    token[key]['sno'] = args[0]
    token[key]['pwd'] = args[1]
    response['text'] = '绑定账号成功'
    print token 
    return jsonify(response)

def logout():
    key = request.form['user_id']
    token.pop(key, None)
    response['text'] = '解除绑定'
    print token
    return jsonify(response)

def online():
    key = request.form['user_id']
    if key in token:
        response['text'] = '已经绑定账号'
        return jsonify(response)
    response['text'] = '尚未绑定账号'
    return jsonify(response)