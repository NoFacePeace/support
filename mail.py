#!./venv/bin/python
# -*- coding: UTF-8 -*-

from flask import Blueprint,request,jsonify
import smtplib
from email.mime.text import MIMEText

host = 'smtp.163.com'
user = '13202114414'
password = 'CHT13202114414'

sender = '13202114414@163.com'
receivers = []

text = {
    'response_type': 'ephemeral',
    'text': '',
}

mail = Blueprint('mail', __name__)

@mail.route('/', methods = ['POST'])
def main():
    tmp = request.form['text']
    args = tmp.split(' ')
    receivers.append(args[0])
    sub = args[1].encode(encoding = 'UTF-8')
    print sub
    content = args[2].encode(encoding = 'UTF-8')
    print content
    if (send_mail(receivers, sub, content)):
        text['text'] = 'Successful!!!'
    else:
        text['text'] = 'Failed!!!'
    return jsonify(text)


def send_mail(to_list, sub, content):
    me = '陈浩涛<13202114414@163.com>'
    msg = MIMEText(content, _subtype = 'plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list[0]
    try:
        server = smtplib.SMTP()
        server.connect(host)
        server.login(user, password)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

