#!./venv/bin/python
# -*- coding: UTF-8 -*-

from flask import Blueprint, jsonify, request

todo = Blueprint('todo', __name__)

tasks = [
    {
        'id': 1,
        'title': 'homework',
        'description': 'do homework',
        'done': False,
    },
    {
        'id': 2,
        'title': 'learning',
        'description': 'learning English',
        'done': False
    }
]

text = {
    'response_type': 'ephemeral',
    'text': '',
}

@todo.route('/', methods = ['POST'])
def controller():
    text = request.form['text']
    args = text.split(' ')
    if (args[0] == ''):
        return get_tasks()
    if (args[0] == 'create'):
        return create_task(args)
    if (args[0] == 'update'):
        return update_task(args)
    if (args[0] == 'delete'):
        return delete_task(args)
    return 'hello world'

def get_tasks():
    content = """| id | title | description | state |
    |:-:|:-:|:-:|:-:|
    """
    for task in tasks:
        content += '|' + str(task['id']) + '|' + task['title'] + '|' + task['description'] + '|' + str(task['done']) + '|' + '\n'
    text['text'] = content
    return jsonify(text)

def create_task(args):
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': args[1],
        'description': args[2],
        'done': False
    }
    tasks.append(task)
    text['text'] = 'Successful!!!'
    return jsonify(text)

def update_task(args):
    id = int(args[1])
    task = filter(lambda t: t['id'] == id, tasks)
    task[0]['done'] = True
    text['text'] = 'Successful!!!'
    return jsonify(text)


def delete_task(args):
    id = int(args[1])
    task = filter(lambda t: t['id'] == id, tasks)
    tasks.remove(task[0])
    text['text'] = 'Successful!!!'
    return jsonify(text)