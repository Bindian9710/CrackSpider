# -*- coding: utf-8 -*-
# @Time: 2020/1/15 17:50
# @Version: 1.0
# @Email: nnlcccc@outlook.com
# 代码千万条，整洁第一条，代码不规范，调试两行泪
import time

import requests
import execjs


class Toutiao:

    def __init__(self):
        self.url = 'https://www.toutiao.com/api/pc/feed/'
        self.exec_js()

    def exec_js(self):
        with open('./头条.js','r',encoding='utf-8') as f:
            self.toutiao_js = execjs.compile(f.read())

    def runspider(self):
        AS,CP = self.toutiao_js.call('get_AS_CP')
        _signature = self.toutiao_js.call('get_sign',AS,CP)
        min_behot_time = int(time.time())
        params = {
            'min_behot_time': min_behot_time,
            'category': '__all__',
            'utm_source': 'toutiao',
            'widen': '1',
            'tadrequire': 'true',
            'as': AS,
            'cp': CP,
            '_signature': _signature,
        }
        headers = {
            'authority': 'www.toutiao.com',
            'method': 'GET',
            'path': f'/api/pc/feed/?min_behot_time={min_behot_time}&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as={AS}&cp={CP}&_signature={_signature}',
            'scheme': 'https',
            'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'tt_webid=6782066255303394830; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6782066255303394830; csrftoken=6b52dc3042913a92268e48ff98b3f0ba; s_v_web_id=77fb4c5d86df30ce5a60094511129cdf; __tasessionId=7nmpuqswx1579081708366',
            'referer': 'https://www.toutiao.com/',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        resp = requests.get(self.url,params=params,headers=headers)

        print(resp.json())
        print(resp)
        print(resp.url)

if __name__ == '__main__':
    Toutiao().runspider()