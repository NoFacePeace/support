#!./venv/bin/python
# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def search_book(query, page):
    url = 'http://weixin.library.gdufe.edu.cn/m/weixin/wsearch.action'
    params = {
        'q': query,
        't': 'any',
        'page': page
    }
    res = requests.get(url = url, params = params)
    book = []
    soup = BeautifulSoup(res.text, "html.parser")
    arr = soup.find_all(attrs = {'class': 'weui_media_title'})
    tmp = {}
    for title in arr:
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
    print book
if __name__ == '__main__':
    search_book('php', 1)